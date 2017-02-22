#include <windows.h>
#include <stdio.h>

int main()
{
	int argc;

	LPWSTR commandline = GetCommandLine();
	LPWSTR *args = CommandLineToArgvW(commandline, &argc);

	if (!args)
	{
		printf("CommandLineToArgvW failed: %x\n", GetLastError());
		return 8;
	}

	size_t commlen = wcslen(commandline);
	size_t read_from = wcslen(args[0]) + 2;
	
	if (argc < 2 || read_from >= commlen)
	{
		printf("Invalid command-line: %S (%S)\n", commandline, args[0]);
		printf("Usage: executable-name\n");
		return 6;
	}

	HANDLE us = OpenProcess(PROCESS_VM_READ | PROCESS_VM_WRITE | PROCESS_VM_OPERATION | PROCESS_QUERY_LIMITED_INFORMATION, FALSE, GetCurrentProcessId() );
	if (!us)
	{
		printf("Couldn't open current process: %x\n", GetLastError());
		return 2;
	}

	BOOL is64;
	if (!IsWow64Process(us, &is64))
	{
		printf("Couldn't check for WoW64: %x\n", GetLastError());
		return 9;
	}

	FARPROC addr = GetProcAddress(GetModuleHandle(L"kernel32"), is64 ? "QueryDosDeviceA" : "GetDriveTypeA");
	if (!addr)
	{
		printf("Couldn't get reference address: %x\n", GetLastError());
		return 1;
	}

	const unsigned char x64ref[] = { 0x75, 0x24 };
	const unsigned char x32ref[] = { 0x0f, 0x85, 0x70, 0x01, 0x00, 0x00 };
	char *target;
	const unsigned char *ref;
	int len;
	if (is64)
	{
		target = (char*)(addr)+0x290;
		len = 2;
		ref = &x64ref[0];
	}
	else
	{
		target = (char*)(addr)+0x11c;
		len = 6;
		ref = x32ref;
	}

	unsigned char stuffs[6];
	if (!ReadProcessMemory(us, target, stuffs, len, NULL))
	{
		printf("Couldn't read us: %x\n", GetLastError());
		return 3;
	}

	for (int i = 0; i < len; ++i)
		if (stuffs[i] != ref[i])
		{
			printf("Check byte %i didn't match: %x != %x\n", i, stuffs[i], ref[i]);
			return 4;
		}

	char nops[] = { 0x90, 0x90, 0x90, 0x90, 0x90, 0x90 };

	if (!WriteProcessMemory(us, target, nops, len, NULL))
	{
		printf("Couldn't patch: %x\n", GetLastError());
		return 5;
	}

	STARTUPINFO si = {};
	si.cb = sizeof(STARTUPINFO);
	PROCESS_INFORMATION pi;

	wchar_t *buf = new wchar_t[commlen];
	wcscpy(buf, commandline + read_from);

	if (!CreateProcess(NULL, buf, NULL, NULL, FALSE, 0, NULL, NULL, &si, &pi))
	{
		printf("CreateProcess failed: %x\n", GetLastError());
		return 7;
	}
}
