title: Adobe GIL and <windows.h>
slug: adobe-gil-and-windowsh
date: 2007-01-10 04:14:32+00:00

I've been playing with <a href="http://opensource.adobe.com/gil/">Adobe <abbr title="Generic Image Library">GIL</abbr></a>, following it's inclusion into <a href="http://boost.org/">Boost</a>, and I've been getting some <em>fun</em> compile errors in relation to <code>&lt;windows.h&gt;</code>. Note that, even if you aren't including <code>&lt;windows.h&gt;</code>, some of the boost headers do.

Here lies: What not to do, so you don't waste hours on it like I did.

<strong>Test-case</strong>:
<pre>int main()
{
	::gil::rgb8_image_t a;
	::gil::jpeg_read_and_convert_image("a", a);
}</pre>

<strong>Compiled with</strong> Visual Studio 2005 SP1, Boost 1.33.1 and JPEG 6b (27-Mar-1998):

<pre>cl /EHsc jpegio.cpp /I c:\sdk\libs /I c:\boost\include\boost-1_33_1</pre>

<strong>First attempt</strong>, <code>&lt;windows.h&gt;</code> first:

<pre>#include &lt;windows.h&gt;

#include &lt;gil/core/gil_all.hpp&gt;
#include &lt;gil/extension/io/jpeg_dynamic_io.hpp&gt;
</pre>

<em>Error</em>:

<pre>jpegio.cpp
c:\sdk\libs\gil\core\channel.hpp(90) : warning C4003: not enough actual paramete rs for macro 'min'
c:\sdk\libs\gil\core\channel.hpp(92) : warning C4003: not enough actual paramete rs for macro 'max'
c:\sdk\libs\jmorecfg.h(161) : error C2371: 'INT32' : redefinition; different bas ic types
        C:\Program Files\Microsoft Visual Studio 8\VC\PlatformSDK\include\basetsd.h(62) : see declaration of 'INT32'
c:\sdk\libs\jmorecfg.h(215) : warning C4005: 'FAR' : macro redefinition
        C:\Program Files\Microsoft Visual Studio 8\VC\PlatformSDK\include\windef.h(145) : see previous definition of 'FAR'</pre>

<strong>Second attempt</strong>, other way around, <em>Error</em>:
<pre>jpegio.cpp
C:\Program Files\Microsoft Visual Studio 8\VC\PlatformSDK\include\basetsd.h(62): error C2371: 'INT32' : redefinition; different basic types
        c:\sdk\libs\jmorecfg.h(161) : see declaration of 'INT32'</pre>

<strong>Third attempt</strong>:

<pre>#include &lt;windows.h&gt;
#include &lt;gil/core/gil_all.hpp&gt;

#define XMD_H
#include &lt;gil/extension/io/jpeg_dynamic_io.hpp&gt;
#undef XMD_H</pre>

This should, in theory improve matters, as XMD_H being #defined stops <code>&lt;jmorecfg.h&gt;</code> trying to redeclare INT32.

Oh no.

<em>Error</em>:

<pre>jpegio.cpp
c:\sdk\libs\gil\core\channel.hpp(90) : warning C4003: not enough actual parameters for macro 'min'
c:\sdk\libs\gil\core\channel.hpp(92) : warning C4003: not enough actual parameters for macro 'max'
c:\sdk\libs\jmorecfg.h(215) : warning C4005: 'FAR' : macro redefinition
        C:\Program Files\Microsoft Visual Studio 8\VC\PlatformSDK\include\windef.h(145) : see previous definition of 'FAR'
c:\sdk\libs\gil\core\color_convert.hpp(148) : error C2589: '(' : illegal token on right side of '::'
        c:\sdk\libs\gil\core\color_convert.hpp(221) : see reference to function template instantiation 'void gil::color_converter_default_impl&lt;lt;T1,C1,T2,C2&gt;::operator ()&lt;lt;SrcP,DstP&gt;(const P1 &,P2 &) const' being compiled
        with
        [
            T1=SrcChannel,
            C1=SrcColorSpace,
            T2=DstChannel,
            C2=DstColorSpace,
            SrcP=gil::pixel&lt;lt;gil::bits8,gil::cmyk_t&gt;,
            DstP=gil::pixel&lt;lt;gil::bits8,gil::rgb_t&gt;,
            P1=gil::pixel&lt;lt;gil::bits8,gil::cmyk_t&gt;,
            P2=gil::pixel&lt;lt;gil::bits8,gil::rgb_t&gt;
        ]
        c:\sdk\libs\gil\extension\dynamic_image\../../core/image_view_factory.hpp(71) : see reference to function template instantiation 'void gil::default_color_converter::operator ()&lt;lt;gil::pixel&lt;lt;T,C&gt;,gil::pixel&lt;lt;T,gil::rgb_t&gt;&gt;(const SrcP &,DstP &) const' being compiled
        with
        [
            T=gil::bits8,
            C=gil::cmyk_t,
            SrcP=gil::pixel&lt;lt;gil::bits8,gil::cmyk_t&gt;,
            DstP=gil::pixel&lt;lt;gil::bits8,gil::rgb_t&gt;
        ]
        c:\sdk\libs\gil\extension\dynamic_image\../../core/image_view_factory.hpp(69) : while compiling class template member function 'gil::pixel&lt;lt;T,C&gt; gil::color_convert_deref_fn&lt;lt;SrcConstRefP,DstP,CC&gt;::operator ()(gil::pixel&lt;lt;T,gil::cmyk_t&gt; &) const'
        with
        [
            T=gil::bits8,
            C=gil::rgb_t,
            SrcConstRefP=gil::cmyk8_ref_t,
            DstP=gil::pixel&lt;lt;gil::bits8,gil::rgb_t&gt;,
            CC=gil::default_color_converter
        ]
        c:\sdk\libs\gil\extension\io\jpeg_io_private.hpp(166) : see reference to class template instantiation 'gil::color_convert_deref_fn&lt;lt;SrcConstRefP,DstP,CC&gt;' being compiled
        with
        [
            SrcConstRefP=gil::cmyk8_ref_t,
            DstP=gil::pixel&lt;lt;gil::bits8,gil::rgb_t&gt;,
            CC=gil::default_color_converter
        ]
        c:\sdk\libs\gil\extension\io\jpeg_io_private.hpp(178) : see reference to function template instantiation 'void gil::detail::jpeg_reader_color_convert&lt;lt;CC&gt;::apply&lt;lt;V2&gt;(const View &)' being compiled
        with
        [
            CC=gil::default_color_converter,
            V2=gil::rgb8_view_t,
            View=gil::rgb8_view_t
        ]
        c:\sdk\libs\gil\extension\io\jpeg_io.hpp(147) : see reference to function template instantiation 'void gil::detail::jpeg_reader_color_convert&lt;lt;CC&gt;::read_image&lt;lt;Image&gt;(Image &)' being compiled
        with
        [
            CC=gil::default_color_converter,
            Image=gil::rgb8_image_t
        ]
        jpegio.cpp(12) : see reference to function template instantiation 'void gil::jpeg_read_and_convert_image&lt;lt;gil::rgb8_image_t&gt;(const char *,Image &)' being compiled
        with
        [
            Image=gil::rgb8_image_t
        ]
c:\sdk\libs\gil\core\color_convert.hpp(148) : error C2143: syntax error : missing ')' before '::'
c:\sdk\libs\gil\core\color_convert.hpp(148) : error C2780: 'T gil::channel_invert(T)' : expects 1 arguments - 0 provided
        c:\sdk\libs\gil\core\channel.hpp(235) : see declaration of 'gil::channel_invert'
c:\sdk\libs\gil\core\color_convert.hpp(148) : error C2059: syntax error : ')'
c:\sdk\libs\gil\core\color_convert.hpp(149) : error C2589: '(' : illegal token on right side of '::'
c:\sdk\libs\gil\core\color_convert.hpp(149) : error C2143: syntax error : missing ')' before '::'
c:\sdk\libs\gil\core\color_convert.hpp(149) : error C2780: 'T gil::channel_invert(T)' : expects 1 arguments - 0 provided
        c:\sdk\libs\gil\core\channel.hpp(235) : see declaration of 'gil::channel_invert'
c:\sdk\libs\gil\core\color_convert.hpp(149) : error C2059: syntax error : ')'
c:\sdk\libs\gil\core\color_convert.hpp(150) : error C2589: '(' : illegal token on right side of '::'
c:\sdk\libs\gil\core\color_convert.hpp(150) : error C2143: syntax error : missing ')' before '::'
c:\sdk\libs\gil\core\color_convert.hpp(150) : error C2780: 'T gil::channel_invert(T)' : expects 1 arguments - 0 provided
        c:\sdk\libs\gil\core\channel.hpp(235) : see declaration of 'gil::channel_invert'
c:\sdk\libs\gil\core\color_convert.hpp(150) : error C2059: syntax error : ')'</pre>

...

<strong>Fourth attempt</strong>, the "right" way:

<pre>#include &lt;gil/core/gil_all.hpp&gt;

#define XMD_H
#include &lt;gil/extension/io/jpeg_dynamic_io.hpp&gt;
#undef XMD_H

#include &lt;windows.h&gt;</pre>

This works as intended.

<strong>Solutions?</strong>

Assuming that we're not going to get the JPEG code patched, the INT32 definition from <code>&lt;windows.h&gt;</code> comes from <code>&lt;basetsd.h&gt;</code>, which declares the <code>BASETSD</code>_H header-guard macro.. it'd be nice if GIL issued an explanation of what was going to go horribly wrong, instead of that lovely template error in test three?