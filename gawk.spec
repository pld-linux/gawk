Summary:	The GNU version of the awk text processing utility
Summary(de):	Die GNU-Version des AWK-Textverarbeitungsutilitys
Summary(fr):	Traitement de texte des utilitaires GNU
Summary(pl):	Wersja GNU awk - narzêdzia do obróbki tekstów
Summary(tr):	GNU araçlarý metin düzenleyici
Name:		gawk
Version:	3.0.4
Release:	3
Copyright:	GPL
Group:		Utilities/Text
Group(pl):	Narzêdzia/Tekst
Source0:	ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		gawk-unaligned.patch
Patch1:		gawk-info.patch
Patch2:		gawk-mktemp.patch
Patch3:		gawk-DESTDIR.patch
Requires:	mktemp
Requires:	sed
Prereq:		/usr/sbin/fix-info-dir
Buildroot:	/tmp/%{name}-%{version}-root

%define		_libexecdir	%{_prefix}/lib
%define		_libdir		%{_prefix}/lib
%define		_exec_prefix	/

%description
The gawk packages contains the GNU version of awk, a text processing
utility. Awk interprets a special-purpose programming language to do quick
and easy text pattern matching and reformatting jobs. Gawk should be
upwardly compatible with the Bell Labs research version of awk and is almost
completely compliant with the 1993 POSIX 1003.2 standard for awk.

Install the gawk package if you need a text processing utility. Gawk is
considered to be a standard Linux tool for processing text.
                                                                                                              
%description -l de
Das gawk-Paket enthält die GNU-Version von awk, einem
Textverarbeitungs-Utility. Awk interpretiert eine spezielle
Programmiersprache, um Textmuster zu suchen, und neu zu formatieren. Gawk
ist kompatibel zu der Bell Labs research-Version von awk, und ist fast
kompatibel zum 1993 POSIX 1003.2-awk-Standard.

Installieren Sie gawk, wenn Sie ein Textverarbeitungsutility brauchen.

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
siê do obróbki plików tekstowych. Jest to jedno z podstawowych narzêdzi
systemu Linux.

%description -l tr
Gawk metin dosyalarýný iþlemek için kullanýlan standart Linux araçlarýndan
biridir.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/bin

make install \
	DESTDIR=$RPM_BUILD_ROOT 

echo ".so gawk.1" > $RPM_BUILD_ROOT%{_mandir}/man1/awk.1
ln -sf %{_bindir}/gawk $RPM_BUILD_ROOT/usr/bin/awk 
ln -sf %{_bindir}/gawk $RPM_BUILD_ROOT/usr/bin/gawk 

gzip -9f $RPM_BUILD_ROOT{%{_infodir}/gawk.info*,%{_mandir}/man1/*} \
	README ACKNOWLEDGMENT FUTURES LIMITATIONS NEWS PORTS \
	README_d/README.linux POSIX.STD

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz README_d/README.linux.gz doc/*.ps.gz
%attr(755,root,root) /usr/bin/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*info*
%attr(755,root,root) %{_libdir}/awk
%{_datadir}/awk
