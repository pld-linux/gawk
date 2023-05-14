#
# Conditional build
%bcond_without	tests	# do not perform "make check"

Summary:	The GNU version of the awk text processing utility
Summary(de.UTF-8):	Die GNU-Version des AWK-Textverarbeitungsutilitys
Summary(es.UTF-8):	Utilitarios GNU para manipulación de archivos texto
Summary(fr.UTF-8):	Traitement de texte des utilitaires GNU
Summary(ja.UTF-8):	GNU バージョンの awk テキスト処理ユーティリティー
Summary(pl.UTF-8):	Wersja GNU awk - narzędzia do obróbki tekstów
Summary(pt_BR.UTF-8):	Utilitários GNU para manipulação arquivos texto
Summary(ru.UTF-8):	GNU версия утилиты обработки текстов awk
Summary(tr.UTF-8):	GNU araçları metin düzenleyici
Summary(uk.UTF-8):	GNU версія утиліти обробки текстів awk
Name:		gawk
Version:	5.2.2
Release:	1
License:	GPL v3+
Group:		Applications/Text
Source0:	https://ftp.gnu.org/gnu/gawk/%{name}-%{version}.tar.lz
# Source0-md5:	9a28be7a094eba63e738df33341e3c90
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	80753d75be0f469f70e8c90e75121a9c
Patch0:		%{name}-info.patch
Patch1:		%{name}-shutup.patch
Patch2:		no-pty-test.patch
URL:		http://www.gnu.org/software/gawk/
BuildRequires:	autoconf >= 2.71
BuildRequires:	autoconf-archive
BuildRequires:	automake >= 1:1.16
BuildRequires:	gettext-tools >= 0.20.2
BuildRequires:	gmp-devel
BuildRequires:	libsigsegv-devel
BuildRequires:	lzip
BuildRequires:	mpfr-devel
BuildRequires:	readline-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo >= 7.0.1
Requires:	mktemp
Requires:	sed
Obsoletes:	gawk-doc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gawk packages contains the GNU version of awk, a text processing
utility. Awk interprets a special-purpose programming language to do
quick and easy text pattern matching and reformatting jobs. Gawk
should be upwardly compatible with the Bell Labs research version of
awk and is almost completely compliant with the 1993 POSIX 1003.2
standard for awk.

%description -l de.UTF-8
Das gawk-Paket enthält die GNU-Version von awk, einem
Textverarbeitungs-Utility. Awk interpretiert eine spezielle
Programmiersprache, um Textmuster zu suchen, und neu zu formatieren.
Gawk ist kompatibel zu der Bell Labs research-Version von awk, und ist
fast kompatibel zum 1993 POSIX 1003.2-awk-Standard.

%description -l es.UTF-8
Este es el GNU Awk. Debe ser compatible con la versión de pesquisa de
awk del Bell Labs. Es casi completamente vinculado con el padrón 1993
POSIX 1003.2 para awk. Gawk puede ser usado para procesar archivos
texto y se considera una herramienta padrón del Linux.

%description -l fr.UTF-8
awk de GNU, compatible vers le haut avec les versions awk des Bell
Labs. Il est presque totalement conforme au standard 1993 POSIX 1003.2
de awk.

%description -l ja.UTF-8
gawk パッケージは GNU バージョンの、テキスト処理ユーティリティー
である awk を含んでいます。awk は素早く、容易なパターンマッチングと
整形処理をするための特殊な目的の言語です。gawk はベル研のバージョンの
awk と上位互換で、awk の 1993 POSIX 1003.2 標準に完全に合致します。

%description -l pl.UTF-8
Pakiet zawiera implementację GNU interpretera języka awk, który
powinien być kompatybilny z aplikacją o tej samej nazwie zrobioną
przez Bell Labs. GNU awk jest w pełni zgodny ze standardem 1993 POSIX
1003.2.

Gawk (GNU awk) jest zaawansowanym językiem skryptowym, doskonale
nadającym się do obróbki plików tekstowych. Jest to jedno z
podstawowych narzędzi systemu Linux.

%description -l pt_BR.UTF-8
Este é o GNU Awk. Ele deve ser compatível com a versão de pesquisa de
awk do Bell Labs. Ele é quase completamente vinculado com o padrão
1993 POSIX 1003.2 para awk. Gawk pode ser usado para processar
arquivos texto e é considerado uma ferramenta padrão do Linux.

%description -l ru.UTF-8
Пакет gawk содержит GNU версию awk, утилиты обработки текстов. awk
интерпретирует специализированный язык программирования для быстрого и
легкого выполнения работ по сопоставлению с шаблонами и
переформатированию текстов. Gawk должен быть совместим с версией awk
от Bell Labs и практически полностью отвечает стандарту 1993 POSIX
1003.2 на awk.

%description -l tr.UTF-8
Gawk metin dosyalarını işlemek için kullanılan standart Linux
Araçlarından biridir.

%description -l uk.UTF-8
Пакет gawk містить GNU версію awk, утиліти обробки текстів. awk
інтерпретує спеціалізовану мову програмування для швидкого та легкого
виконання робіт по співставленню з шаблонами та переформатуванню
текстів. Gawk має бути сумісним з версією awk від Bell Labs і
практично повністю відповідає стандарту 1993 POSIX 1003.2 на awk.

%package devel
Summary:	Header files for gawk
Summary(pl.UTF-8):	Pliki nagłówkowe dla gawka
Group:		Development/Libraries

%description devel
This is the package containing the header files for gawk.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe dla gawka.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%{__rm} po/stamp-po

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
cd extension
%{__libtoolize}
%{__aclocal} -I m4 -I ../m4
%{__autoconf}
%{__autoheader}
%{__automake}
cd ..
%configure \
	--datadir=%{_libdir}

%{__make} -j1

%{?with_tests:%{__make} -j1 check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_bindir}/gawk-%{version}
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

# mawk provides system wide 'awk'
%{__rm} $RPM_BUILD_ROOT%{_bindir}/awk

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/README.gawk-non-english-man-pages
# igawk is declared as obsolete since 4.0.0, dropped in 4.2.0
%{__rm} $RPM_BUILD_ROOT%{_mandir}/{es,fr,it,ja,pl}/man1/igawk.1

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS POSIX.STD README
%attr(755,root,root) %{_bindir}/gawk
%attr(755,root,root) %{_bindir}/gawkbug
%dir %{_libdir}/gawk
%attr(755,root,root) %{_libdir}/gawk/*.so
%dir %{_libdir}/awk
%{_libdir}/awk/*.awk
%if "%{_libexecdir}" != "%{_libdir}"
%dir %{_libexecdir}/awk
%endif
%attr(755,root,root) %{_libexecdir}/awk/grcat
%attr(755,root,root) %{_libexecdir}/awk/pwcat
/etc/profile.d/gawk.csh
/etc/profile.d/gawk.sh
%{_mandir}/man1/gawk.1*
%{_mandir}/man1/gawkbug.1*
%{_mandir}/man1/pm-gawk.1*
%{_mandir}/man3/filefuncs.3am*
%{_mandir}/man3/fnmatch.3am*
%{_mandir}/man3/fork.3am*
%{_mandir}/man3/inplace.3am*
%{_mandir}/man3/ordchr.3am*
%{_mandir}/man3/readdir.3am*
%{_mandir}/man3/readfile.3am*
%{_mandir}/man3/revoutput.3am*
%{_mandir}/man3/revtwoway.3am*
%{_mandir}/man3/rwarray.3am*
%{_mandir}/man3/time.3am*
%lang(es) %{_mandir}/es/man1/gawk.1*
%lang(fr) %{_mandir}/fr/man1/gawk.1*
%lang(it) %{_mandir}/it/man1/gawk.1*
%lang(ja) %{_mandir}/ja/man1/gawk.1*
%lang(pl) %{_mandir}/pl/man1/gawk.1*
%{_infodir}/gawk*.info*
%{_infodir}/gawk*.jpg
%{_infodir}/gawk*.png
%{_infodir}/pm-gawk.info*

%files devel
%defattr(644,root,root,755)
%{_includedir}/gawkapi.h
