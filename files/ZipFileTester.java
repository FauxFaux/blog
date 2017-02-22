import java.io.IOException;
import java.io.InputStream;
import java.lang.reflect.InvocationTargetException;
import java.util.Enumeration;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

class ZipFileTester {
	private static String arg;

	public static void main(String[] args) throws InstantiationException, IllegalAccessException,
		InvocationTargetException, NoSuchMethodException, IOException, InterruptedException {
		if (1 != args.length) {
			System.err.println("Usage: zipfile");
			return;
		}
		arg = args[0];

		final int OPS = 64;

		// WARMING
		for (int i = 0; i < 5; ++i) {
			builtIn();
			pureJava();
		}

		System.out.println("threads\tsync\tunsync\tpure");

		for (int threads = 1; threads <= 8; threads *= 2) {
			System.out.print(threads + "\t");

			final int loops = OPS / threads;

			// synched
			{
				final ExecutorService ex = Executors.newFixedThreadPool(threads);
				long start = System.nanoTime();
				for (int j = 0; j < threads; ++j)
					ex.submit(new Callable<Void>() {
						@Override public Void call() throws Exception {
							synchronized (ZipFileTester.class) {
								for (int i = 0; i < loops; ++i)
									builtIn();
							}
							return null;
						}
					});
				ex.shutdown();
				ex.awaitTermination(Long.MAX_VALUE, TimeUnit.DAYS);
				System.out.print((System.nanoTime() - start)/1e9 + "\t");
			}

			// unsynched
			{
				final ExecutorService ex = Executors.newFixedThreadPool(threads);
				final long start = System.nanoTime();
				for (int j = 0; j < threads; ++j)
					ex.submit(new Callable<Void>() {
						@Override public Void call() throws Exception {
							for (int i = 0; i < loops; ++i)
								builtIn();
							return null;
						}
					});
				ex.shutdown();
				ex.awaitTermination(Long.MAX_VALUE, TimeUnit.DAYS);
				System.out.print((System.nanoTime() - start) / 1e9 + "\t");
			}

			// pure java
			{
				final ExecutorService ex = Executors.newFixedThreadPool(threads);
				final long start = System.nanoTime();
				for (int j = 0; j < threads; ++j)
					ex.submit(new Callable<Void>() {
						@Override public Void call() throws Exception {
							for (int i = 0; i < loops; ++i)
								pureJava();
							return null;
						}
					});
				ex.shutdown();
				ex.awaitTermination(Long.MAX_VALUE, TimeUnit.DAYS);
				System.out.println((System.nanoTime() - start) / 1e9);
			}
		}
	}

	private static int pureJava() throws InstantiationException, IllegalAccessException, InvocationTargetException,
			NoSuchMethodException, IOException {
		return run(net.sf.jazzlib.ZipFile.class);
	}

	private static int builtIn() throws InstantiationException, IllegalAccessException, InvocationTargetException,
			NoSuchMethodException, IOException {
		return run(java.util.zip.ZipFile.class);
	}

	private static int run(Class<?> cls) throws InstantiationException, IllegalAccessException,
			InvocationTargetException, NoSuchMethodException, IOException {
		final Object zf = cls.getConstructor(String.class).newInstance(arg);
		final Enumeration<?> e = (Enumeration<?>) zf.getClass().getMethod("entries").invoke(zf);
		final byte[] by = new byte[4096];
		int output = 0;
		while (e.hasMoreElements()) {
			Object ze = e.nextElement();
			final String n = (String) ze.getClass().getMethod("getName").invoke(ze);
			output += n.hashCode();
			if (n.contains("e")) {
				InputStream is = (InputStream) zf.getClass()
					.getMethod("getInputStream", ze.getClass()).invoke(zf, ze);
				output += (Boolean) ze.getClass().getMethod("isDirectory").invoke(ze) ? 1 : 0;
				int rd;
				while ((rd = is.read(by)) != -1)
					for (int i = 0; i < rd; ++i)
						output += by[i];
			}
		}
		return output;
	}

}
