title: Rebuilding Debian with Java 9
slug: java-9-rebuild
date: 2017-07-02T22:11:12+02:00

It's about three months until
[Java 9 is supposed to be released](http://www.java9countdown.xyz/).
Debian contains around 1,200 packages that build against Java 8.
I have been trying to build them with Java 9.

It's not been going well.

[The first attempt](https://lists.debian.org/debian-java/2017/06/msg00038.html)
found an 87% failure rate, the majority of which were either:

 * toolchain issues (which are for Debian to fix)
    (e.g. [maven/guice needing new cglib](https://bugs.debian.org/866411)).
 * `-source` and `-target` being old, unsupported values.

This is too bad to get an idea of what's actually broken, so I gave up.


[The second attempt](https://lists.debian.org/debian-java/2017/07/msg00010.html)
has gone better, only 57% failures. This had a number of issues fixed, but
there's still a large number of problems masked by toolchain failures.

However, some real Java 9 breakages are coming to the fore!

 * 90 packages are hitting [module-based accessibility rules](https://rbuild.fau.xxx/2017-07-02/modules/),
    although maybe many of these are bugs in `gradle`. These are the kind of
    bug that it may be hard to fix in your own software, so it's slightly
    worrying to see so many of them.
 * 15 packages are using [underscore or enum as a keyword](https://rbuild.fau.xxx/2017-07-02/keyword/),
    which hopefully should be easy to fix everywhere.
 * 9 packages have new [compile failures around casting](https://rbuild.fau.xxx/2017-07-02/cast/),
    which may be compiler improvements, or bugs. Exciting!

Oh, and 135 packages have [an unknown problem](https://rbuild.fau.xxx/2017-07-02/unknown/),
so maybe there's a whole other class of bug I've missed.

This is (obviously) an ongoing [project](https://github.com/FauxFaux/debjdk9),
but I thought I'd write up what I'd seen so far.

Also, I wanted to mention how cool it was to hack up a dashboard for your
[ghetto make/Docker build process](https://github.com/FauxFaux/debjdk9/blob/master/Makefile)
in [ghetto shell](https://github.com/FauxFaux/debjdk9/blob/d2a4a6c692211f7e819a4909d78d2d060d2a7a24/classify.sh),
although slightly less ghetto than the
[previous shell](https://github.com/FauxFaux/debjdk9/blob/fe991263eb22510fa8ac45f2d8978dc667784a46/classify.sh).
This needs a wide monitor / small font to look okay:


    Every 2.0s: ./classify.sh

    ascii           cast            deps            doclint         javadoc         keyword         modules         unknown         version
    47 total        9 total         203 total       82 total        165 total       15 total        83 total        114 total       206 total
    ====            ====            ====            ====            ====            ====            ====            ====            ====
    antelope        charactermanaj  access-*hecker  android*-tools  access-*hecker  avalon-*mework  activem*otobuf  adql            389-adm*onsole
    axis            dom4j           activem*tiveio  antlr4          akuma           axis            android*ork-23  aspectj         389-ds-console
    azureus         electric        activemq        args4j          animal-sniffer  biojava-live    android*dalvik  aspectj*plugin  airport-utils
    clirr           findbugs        activem*otobuf  bindex          annotat*ndexer  bnd             android*oclava  bouncycastle    android*-tools
    cmdreader       jajuk           afterburner.fx  cdi-api         antlr3          dbus-java       android*silver  bsh             antlr
    cortado         jsymphonic      akuma           classycle       apache-log4j2   jalview         android*inding  closure*mpiler  artemis
    cronometer      libjaud*r-java  animal-sniffer  commons-math3   apache-mime4j   javacc4         android*ibcore  cofoja          beansbinding
    dita-ot         olap4j          annotat*ndexer  ditaa           async-h*client  java-gnome      android*ibrary  commons-jcs     bindex
    eclipselink     sweethome3d     antlr3          felix-g*-shell  axmlrpc         jmol            android*apksig  convers*ruptor  biojava-live
    eclipse                         antlr4          fest-assert     bcel            jruby-openssl   android*s-base  davmail         biomaj
    entagged                        apache-log4j2   fest-reflect    bridge-*jector  libcomm*g-java  android*ls-swt  diffoscope      brig
    fop                             args4j          fest-util       bsaf            libxml-*1-java  android*helper  dnsjava         brltty
    geronim*0-spec                  atinjec*jsr330  ganymed-ssh2    build-h*plugin  libxpp2-java    ant             dumbster        cadencii
    imagej                          bcel            gentlyw*-utils  canl-java       mvel            apktool         eclipse*nyedit  castor
    jasmin-sable                    bridge-*jector  glassfish       cglib           squareness      basex           eclipse-cdt     cdi-api
    jas                             build-h*plugin  hdf5            commons*nutils                  bintray*t-java  eclipse*config  ceph
    jasypt                          carrots*h-hppc  hessian         commons*ration                  biojava4-live   eclipse-eclox   cobertura
    javacc4                         cglib           intelli*ations  commons-csv                     easybind        eclipse-emf     coco-java
    javaparser                      checkstyle      jacksum         commons-io                      eclipse-mylyn   eclipse-gef     colorpicker
    jets3t                          codenarc        jcm             commons*vaflow                  eclipse-wtp     eclipse*clipse  commons*client
    jgromacs                        commons*nutils  jfugue          commons-jci                     eclipse-xsd     eclipse*es-api  concurr*t-dfsg
    king                            commons*ration  jmock           commons-math                    freeplane       eclipse-rse     cvc3
    knopfle*h-osgi                  commons-csv     jnr-ffi         cssparser                       gant            eclipse*clipse  db5.3
    libcds-*t-java                  commons-io      jpathwatch      csvjdbc                         gradle-*plugin  emma-coverage   dbus-java
    libcomm*g-java                  commons*vaflow  jsurf-alggeo    dirgra                          gradle          gdcm            dicomscope
    libidw-java                     commons-jci     jts             dnssecjava                      gradle-*otobuf  geronim*upport  ditaa
    libiscwt-java                   commons-math    libcds-*c-java  dokujclient                     gradle-*plugin  gettext         docbook*-saxon
    libitext-java                   commons-parent  libcomm*c-java  doxia-s*etools                  graxxia         gluegen2        doxia
    libjdbm-java                    commons-vfs     libcomm*4-java  dtd-parser                      groovycsv       gnome-split     easyconf
    libjt400-java                   core-ca*lojure  libcomm*2-java  easymock                        groovy          h2database      excalib*logger
    libstax-java                    cssparser       libhac-java     felix-b*sitory                  gs-collections  ha-jdbc         excalib*logkit
    libvldo*g-java                  data-xm*lojure  libhtml*r-java  felix-f*mework                  htsjdk          hdrhistogram    f2j
    libxpp3-java                    dirgra          libirclib-java  felix-g*ommand                  ice-bui*gradle  icu4j           felix-osgi-obr
    livetri*jsr223                  dnssecjava      libjaba*t-java  felix-g*untime                  insubstantial   icu4j-4.2       fontchooser
    mathpiper                       dokujclient     libjgoo*n-java  felix-shell                     ivyplusplus     icu4j-4.4       ganymed-ssh2
    maven-a*helper                  doxia           libjhla*s-java  felix-s*ll-tui                  jabref          icu4j-49        gentlyw*-utils
    metastudent                     doxia-s*etools  libjoda*e-java  felix-utils                     jackson*tabind  istack-commons  geogebra
    naga                            dtd-parser      libjsonp-java   geronim*0-spec                  jackson*-guava  jakarta-jmeter  gridengine
    ognl                            easymock        libjsr1*y-java  geronim*1-spec                  java3d          janino          healpix-java
