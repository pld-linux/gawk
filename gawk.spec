Summary:	The GNU version of the awk text processing utility
Summary(de):	Die GNU-Version des AWK-Textverarbeitungsutilitys
Summary(es):	Utilitarios GNU para manipulación de archivos texto
Summary(fr):	Traitement de texte des utilitaires GNU
Summary(ja):	GNU ¥Ð¡¼¥¸¥ç¥ó¤Î awk ¥Æ¥­¥¹¥È½èÍý¥æ¡¼¥Æ¥£¥ê¥Æ¥£¡¼
Summary(pl):	Wersja GNU awk - narzêdzia do obróbki tekstów
Summary(pt_BR):	Utilitários GNU para manipulação arquivos texto
Summary(ru):	GNU ×ÅÒÓÉÑ ÕÔÉÌÉÔÙ ÏÂÒÁÂÏÔËÉ ÔÅËÓÔÏ× awk
Summary(tr):	GNU araçlarý metin düzenleyici
Summary(uk):	GNU ×ÅÒÓ¦Ñ ÕÔÉÌ¦ÔÉ ÏÂÒÏÂËÉ ÔÅËÓÔ¦× awk
Name:		gawk
Version:	3.1.1
Release:	3
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-info.patch
Patch1:		%{name}-newsecurity.patch
Patch2:		%{name}-shutup.patch
Patch3:		%{name}-pmake.patch
Patch4:		%{name}-ac.patch
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
Este es el GNU Awk. Debe ser compatible con la versión de pesquisa de
awk del Bell Labs. Es casi completamente vinculado con el padrón 1993
POSIX 1003.2 para awk. Gawk puede ser usado para procesar archivos
texto y se considera una herramienta padrón del Linux.

%description -l fr
awk de GNU, compatible vers le haut avec les versions awk des Bell
Labs. Il est presque totalement conforme au standard 1993 POSIX 1003.2
de awk.

%description -l ja
gawk ¥Ñ¥Ã¥±¡¼¥¸¤Ï GNU ¥Ð¡¼¥¸¥ç¥ó¤Î¡¢¥Æ¥­¥¹¥È½èÍý¥æ¡¼¥Æ¥£¥ê¥Æ¥£¡¼
¤Ç¤¢¤ë awk ¤ò´Þ¤ó¤Ç¤¤¤Þ¤¹¡£awk ¤ÏÁÇÁá¤¯¡¢ÍÆ°×¤Ê¥Ñ¥¿¡¼¥ó¥Þ¥Ã¥Á¥ó¥°¤È
À°·Á½èÍý¤ò¤¹¤ë¤¿¤á¤ÎÆÃ¼ì¤ÊÌÜÅª¤Î¸À¸ì¤Ç¤¹¡£gawk ¤Ï¥Ù¥ë¸¦¤Î¥Ð¡¼¥¸¥ç¥ó¤Î
awk ¤È¾å°Ì¸ß´¹¤Ç¡¢awk ¤Î 1993 POSIX 1003.2 É¸½à¤Ë´°Á´¤Ë¹çÃ×¤·¤Þ¤¹¡£

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

%description -l ru
ðÁËÅÔ gawk ÓÏÄÅÒÖÉÔ GNU ×ÅÒÓÉÀ awk, ÕÔÉÌÉÔÙ ÏÂÒÁÂÏÔËÉ ÔÅËÓÔÏ×. awk
ÉÎÔÅÒÐÒÅÔÉÒÕÅÔ ÓÐÅÃÉÁÌÉÚÉÒÏ×ÁÎÎÙÊ ÑÚÙË ÐÒÏÇÒÁÍÍÉÒÏ×ÁÎÉÑ ÄÌÑ ÂÙÓÔÒÏÇÏ É
ÌÅÇËÏÇÏ ×ÙÐÏÌÎÅÎÉÑ ÒÁÂÏÔ ÐÏ ÓÏÐÏÓÔÁ×ÌÅÎÉÀ Ó ÛÁÂÌÏÎÁÍÉ É
ÐÅÒÅÆÏÒÍÁÔÉÒÏ×ÁÎÉÀ ÔÅËÓÔÏ×. Gawk ÄÏÌÖÅÎ ÂÙÔØ ÓÏ×ÍÅÓÔÉÍ Ó ×ÅÒÓÉÅÊ awk
ÏÔ Bell Labs É ÐÒÁËÔÉÞÅÓËÉ ÐÏÌÎÏÓÔØÀ ÏÔ×ÅÞÁÅÔ ÓÔÁÎÄÁÒÔÕ 1993 POSIX
1003.2 ÎÁ awk.

%description -l tr
Gawk metin dosyalarýný iþlemek için kullanýlan standart Linux
Araçlarýndan biridir.

%description -l uk
ðÁËÅÔ gawk Í¦ÓÔÉÔØ GNU ×ÅÒÓ¦À awk, ÕÔÉÌ¦ÔÉ ÏÂÒÏÂËÉ ÔÅËÓÔ¦×. awk
¦ÎÔÅÒÐÒÅÔÕ¤ ÓÐÅÃ¦ÁÌ¦ÚÏ×ÁÎÕ ÍÏ×Õ ÐÒÏÇÒÁÍÕ×ÁÎÎÑ ÄÌÑ Û×ÉÄËÏÇÏ ÔÁ ÌÅÇËÏÇÏ
×ÉËÏÎÁÎÎÑ ÒÏÂ¦Ô ÐÏ ÓÐ¦×ÓÔÁ×ÌÅÎÎÀ Ú ÛÁÂÌÏÎÁÍÉ ÔÁ ÐÅÒÅÆÏÒÍÁÔÕ×ÁÎÎÀ
ÔÅËÓÔ¦×. Gawk ÍÁ¤ ÂÕÔÉ ÓÕÍ¦ÓÎÉÍ Ú ×ÅÒÓ¦¤À awk ×¦Ä Bell Labs ¦
ÐÒÁËÔÉÞÎÏ ÐÏ×Î¦ÓÔÀ ×¦ÄÐÏ×¦ÄÁ¤ ÓÔÁÎÄÁÒÔÕ 1993 POSIX 1003.2 ÎÁ awk.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-nls
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_bindir}/gawk-%{version}

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
%doc AUTHORS README FUTURES LIMITATIONS NEWS PROBLEMS 
%doc README_d/README.linux POSIX.STD
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
