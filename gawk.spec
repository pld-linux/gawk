Summary:	GNU utilities text processor.
Summary(de):	GNU-Utilities Text-Prozessor
Summary(fr):	Traitement de texte des utilitaires GNU
Summary(pl):	Narzêdzia do obróbki plików tekstowych z GNU
Summary(tr):	GNU araçlarý metin düzenleyici
Name:		gawk
Version:	3.0.3
Release:	8
Copyright:	GPL
Group:		Utilities/Text
Group(pl):	Narzêdzia/Tekst
Source0:	ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Source1:	ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}-ps.tar.gz
Patch0:		gawk-unaligned.patch
Patch1:		gawk-info.patch
Buildroot:	/tmp/%{name}-%{version}-root

%description
This is GNU Awk. It should be upwardly compatible with the Bell Labs
research version of awk.  It is almost completely compliant with the
1993 POSIX 1003.2 standard for awk.

Gawk can be used to process text files and is considered a standard
Linux tool.

%description -l de
Dies ist GNU Awk. Es sollte aufwärtskompatibel mit der Bell Labs-
Version von awk sein. Es ist fast vollständig konform mit dem 1993 
POSIX 1003.2-Standard für awk.
Gawk läßt sich zum Verarbeiten von Textdateien einsetzen und gilt als
ein Standard-Linux-Tool.

%description -l fr
awk de GNU, compatible vers le haut avec les versions awk des Bell Labs.
Il est presque totalement conforme au standard 1993 POSIX 1003.2 de awk.

gawk sert à traiter les fichiers texte est est considéré comme un outil
standard de Linux.

%description -l pl
Pakiet zawiera implementacjê GNU interpretera jêzyka awk, który powinien
byæ kompatybilny z aplikacj± o tej samej nazwie zrobion± przez Bell Labs.
GNU awk jest w pe³ni zgodny ze standardem 1993 POSIX 1003.2.

Gawk (GNU awk) jest zaawansowanym jêzykiem skryptowym, doskonale nadaj±cym
sie do obróbki plików tekstowych. Jest to jedno z podstawowych narzêdzi
systemu Linux.

%description -l tr
Gawk metin dosyalarýný iþlemek için kullanýlan standart Linux araçlarýndan
biridir.

%prep
%setup -q -b 1
%patch0 -p1
%patch1 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/bin

make install prefix=$RPM_BUILD_ROOT/usr bindir=$RPM_BUILD_ROOT/bin

echo ".so gawk.1" > $RPM_BUILD_ROOT%{_mandir}/man1/awk.1
ln -sf /bin/gawk $RPM_BUILD_ROOT/usr/bin/awk 
ln -sf /bin/gawk $RPM_BUILD_ROOT/usr/bin/gawk 

gzip -9f $RPM_BUILD_ROOT/usr/{info/gawk.info*,man/man1/*} \
	README ACKNOWLEDGMENT FUTURES LIMITATIONS NEWS PORTS \
	README_d/README.linux POSIX.STD doc/gawk.ps doc/awkcard.ps

%post
/sbin/install-info %{_infodir}/gawk.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/gawk.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz README_d/README.linux.gz doc/*.ps.gz
%attr(755,root,root) /bin/*
%attr(755,root,root) /usr/bin/*
%{_mandir}/man1/*
%{_infodir}/*info*
%attr(755,root,root) /usr/libexec/awk
%{_datadir}/awk

%changelog
* Mon Apr 19 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.0.3-8]
- recompiles on new rpm.

* Wed Apr 14 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.0.3-7]
- removed man group from man pages,
- gzipping %doc.

* Sat Jan 02 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.0.3-5]
- added %post, %preun with {un}registering gawk info
  pages (added gawk-info.patch),
- added gzipping man pages,
- added using LDFLAGS="-s" to ./configure enviroment.

* Mon Oct 26 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.0.3-4]
- awk(1) man page is now maked as nroff include to gawk(1) instead
  making sym link to gawk.1 (this allow compress man pages in future),
- removed INSTALL and COPYING from %doc (copyright statment is in Copyright
  field).

* Sun Jul 19 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- added pl translation,
- added -q %setup parameter,
- buildroot canged to /tmp/%{name}-%{version}-root.

* Wed May 06 1998 Cristian Gafton <gafton@redhat.com>
- don't package %{_infodir}/dir

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 3.0.3
- added documentation and buildroot

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
