Summary:	The GNU version of the awk text processing utility
Summary(de):	Die GNU-Version des AWK-Textverarbeitungsutilitys
Summary(es): Utilitarios GNU para manipulación de archivos texto
Summary(fr):	Traitement de texte des utilitaires GNU
Summary(pl):	Wersja GNU awk - narzêdzia do obróbki tekstów
Summary(tr):	GNU araçlarý metin düzenleyici
Summary(pt_BR): Utilitários GNU para manipulação arquivos texto
Name:		gawk
Version:	3.1.0
Release:	5
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-info.patch
Patch1:		%{name}-newsecurity.patch
Patch2:		%{name}-shutup.patch
Requires:	mktemp
Requires:	sed
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	gawk-doc

%define		_libexecdir	%{_prefix}/lib
%define		_libdir		%{_prefix}/lib

%description
The gawk packages contains the GNU version of awk, a text processing
utility. Awk interprets a special-purpose programming language to do
quick and easy text pattern matching and reformatting jobs. Gawk
should be upwardly compatible with the Bell Labs research version of
awk and is almost completely compliant with the 1993 POSIX 1003.2
standard for awk.

%description -l de
Das gawk-Paket enthält die GNU-Version von awk, einem
Textverarbeitungs-Utility. Awk interpretiert eine spezielle
Programmiersprache, um Textmuster zu suchen, und neu zu formatieren.
Gawk ist kompatibel zu der Bell Labs research-Version von awk, und ist
fast kompatibel zum 1993 POSIX 1003.2-awk-Standard.

%description -l es
Este es el GNU Awk. Debe ser compatible con la versión de pesquisa
de awk del Bell Labs. Es casi completamente vinculado con el padrón
1993 POSIX 1003.2 para awk. Gawk puede ser usado para procesar
archivos texto y se considera una herramienta padrón del Linux.

%description -l fr
awk de GNU, compatible vers le haut avec les versions awk des Bell
Labs. Il est presque totalement conforme au standard 1993 POSIX 1003.2
de awk.

gawk sert à traiter les fichiers texte est est considéré comme un
outil standard de Linux.

%description -l pl
Pakiet zawiera implementacjê GNU interpretera jêzyka awk, który
powinien byæ kompatybilny z aplikacj± o tej samej nazwie zrobion±
przez Bell Labs. GNU awk jest w pe³ni zgodny ze standardem 1993 POSIX
1003.2.

Gawk (GNU awk) jest zaawansowanym jêzykiem skryptowym, doskonale
nadaj±cym siê do obróbki plików tekstowych. Jest to jedno z
podstawowych narzêdzi systemu Linux.

%description -l pt_BR
Este é o GNU Awk. Ele deve ser compatível com a versão de pesquisa de
awk do Bell Labs. Ele é quase completamente vinculado com o padrão
1993 POSIX 1003.2 para awk. Gawk pode ser usado para processar
arquivos texto e é considerado uma ferramenta padrão do Linux.

%description -l tr
Gawk metin dosyalarýný iþlemek için kullanýlan standart Linux
Araçlarýndan biridir.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure2_13 \
	--enable-nls
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

rm -f $RPM_BUILD_ROOT%{_bindir}/gawk-%{version}

gzip -9nf AUTHORS README FUTURES LIMITATIONS NEWS PROBLEMS \
	README_d/README.linux POSIX.STD

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *gz README_d/README.linux.gz 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_infodir}/*info*
%attr(755,root,root) %{_libdir}/awk
%{_datadir}/awk
