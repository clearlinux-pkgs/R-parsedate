#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-parsedate
Version  : 1.2.0
Release  : 7
URL      : https://cran.r-project.org/src/contrib/parsedate_1.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/parsedate_1.2.0.tar.gz
Summary  : Recognize and Parse Dates in Various Formats, Including All ISO
Group    : Development/Tools
License  : GPL-2.0
Requires: R-parsedate-lib = %{version}-%{release}
Requires: R-rematch2
BuildRequires : R-assertthat
BuildRequires : R-cli
BuildRequires : R-rematch2
BuildRequires : R-withr
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
# parsedate — Parse dates from ISO 8601, and guess the format
[![Linux Build Status](https://travis-ci.org/gaborcsardi/parsedate.svg?branch=master)](https://travis-ci.org/gaborcsardi/parsedate)
[![Windows build status](https://ci.appveyor.com/api/projects/status/github/gaborcsardi/parsedate?svg=true)](https://ci.appveyor.com/project/gaborcsardi/parsedate)
[![](http://www.r-pkg.org/badges/version/parsedate)](http://www.r-pkg.org/pkg/parsedate)
[![CRAN RStudio mirror downloads](http://cranlogs.r-pkg.org/badges/parsedate)](https://r-pkg.org/pkg/parsedate)
[![Coverage Status](https://img.shields.io/codecov/c/github/gaborcsardi/parsedate/master.svg)](https://codecov.io/github/gaborcsardi/parsedate?branch=master)

%package lib
Summary: lib components for the R-parsedate package.
Group: Libraries

%description lib
lib components for the R-parsedate package.


%prep
%setup -q -c -n parsedate

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571871343

%install
export SOURCE_DATE_EPOCH=1571871343
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library parsedate
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library parsedate
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library parsedate
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc parsedate || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/parsedate/DESCRIPTION
/usr/lib64/R/library/parsedate/INDEX
/usr/lib64/R/library/parsedate/Meta/Rd.rds
/usr/lib64/R/library/parsedate/Meta/features.rds
/usr/lib64/R/library/parsedate/Meta/hsearch.rds
/usr/lib64/R/library/parsedate/Meta/links.rds
/usr/lib64/R/library/parsedate/Meta/nsInfo.rds
/usr/lib64/R/library/parsedate/Meta/package.rds
/usr/lib64/R/library/parsedate/NAMESPACE
/usr/lib64/R/library/parsedate/NEWS.md
/usr/lib64/R/library/parsedate/R/parsedate
/usr/lib64/R/library/parsedate/R/parsedate.rdb
/usr/lib64/R/library/parsedate/R/parsedate.rdx
/usr/lib64/R/library/parsedate/README.Rmd
/usr/lib64/R/library/parsedate/README.md
/usr/lib64/R/library/parsedate/help/AnIndex
/usr/lib64/R/library/parsedate/help/aliases.rds
/usr/lib64/R/library/parsedate/help/parsedate.rdb
/usr/lib64/R/library/parsedate/help/parsedate.rdx
/usr/lib64/R/library/parsedate/help/paths.rds
/usr/lib64/R/library/parsedate/html/00Index.html
/usr/lib64/R/library/parsedate/html/R.css
/usr/lib64/R/library/parsedate/tests/testthat.R
/usr/lib64/R/library/parsedate/tests/testthat/helper.R
/usr/lib64/R/library/parsedate/tests/testthat/test-corner-cases.R
/usr/lib64/R/library/parsedate/tests/testthat/test-git.r
/usr/lib64/R/library/parsedate/tests/testthat/test-iso8601.r
/usr/lib64/R/library/parsedate/tests/testthat/test-time-zones.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/parsedate/libs/parsedate.so
/usr/lib64/R/library/parsedate/libs/parsedate.so.avx2
/usr/lib64/R/library/parsedate/libs/parsedate.so.avx512
