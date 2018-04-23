#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rstanarm
Version  : 2.17.3
Release  : 3
URL      : https://cran.r-project.org/src/contrib/rstanarm_2.17.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rstanarm_2.17.3.tar.gz
Summary  : Bayesian Applied Regression Modeling via Stan
Group    : Development/Tools
License  : GPL-3.0
Requires: R-rstanarm-lib
Requires: R-BH
Requires: R-Rcpp
Requires: R-RcppEigen
Requires: R-StanHeaders
Requires: R-bayesplot
Requires: R-gamm4
Requires: R-roxygen2
Requires: R-rstantools
Requires: R-shinystan
Requires: R-shinythemes
Requires: R-threejs
BuildRequires : R-BH
BuildRequires : R-Rcpp
BuildRequires : R-RcppEigen
BuildRequires : R-StanHeaders
BuildRequires : R-bayesplot
BuildRequires : R-gamm4
BuildRequires : R-roxygen2
BuildRequires : R-rstantools
BuildRequires : R-shinystan
BuildRequires : R-shinythemes
BuildRequires : R-threejs
BuildRequires : clr-R-helpers

%description
package, which provides the R interface to the Stan C++ library for Bayesian
    estimation. Users specify models via the customary R syntax with a formula and
    data.frame plus some additional arguments for priors.

%package lib
Summary: lib components for the R-rstanarm package.
Group: Libraries

%description lib
lib components for the R-rstanarm package.


%prep
%setup -q -c -n rstanarm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521256734

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521256734
export LANG=C
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rstanarm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rstanarm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rstanarm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library rstanarm|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rstanarm/CITATION
/usr/lib64/R/library/rstanarm/DESCRIPTION
/usr/lib64/R/library/rstanarm/Meta/Rd.rds
/usr/lib64/R/library/rstanarm/Meta/data.rds
/usr/lib64/R/library/rstanarm/Meta/demo.rds
/usr/lib64/R/library/rstanarm/Meta/features.rds
/usr/lib64/R/library/rstanarm/Meta/hsearch.rds
/usr/lib64/R/library/rstanarm/Meta/links.rds
/usr/lib64/R/library/rstanarm/Meta/nsInfo.rds
/usr/lib64/R/library/rstanarm/Meta/package.rds
/usr/lib64/R/library/rstanarm/Meta/vignette.rds
/usr/lib64/R/library/rstanarm/NAMESPACE
/usr/lib64/R/library/rstanarm/NEWS
/usr/lib64/R/library/rstanarm/R/rstanarm
/usr/lib64/R/library/rstanarm/R/rstanarm.rdb
/usr/lib64/R/library/rstanarm/R/rstanarm.rdx
/usr/lib64/R/library/rstanarm/data/Rdata.rdb
/usr/lib64/R/library/rstanarm/data/Rdata.rds
/usr/lib64/R/library/rstanarm/data/Rdata.rdx
/usr/lib64/R/library/rstanarm/demo/ARM_Ch03.R
/usr/lib64/R/library/rstanarm/demo/ARM_Ch04.R
/usr/lib64/R/library/rstanarm/demo/ARM_Ch05.R
/usr/lib64/R/library/rstanarm/demo/ARM_Ch07.R
/usr/lib64/R/library/rstanarm/demo/ARM_Ch08.R
/usr/lib64/R/library/rstanarm/demo/ARM_Ch09.R
/usr/lib64/R/library/rstanarm/demo/ARM_Ch12_13.R
/usr/lib64/R/library/rstanarm/demo/ARM_Ch14.R
/usr/lib64/R/library/rstanarm/demo/CLEANUP.R
/usr/lib64/R/library/rstanarm/demo/SETUP.R
/usr/lib64/R/library/rstanarm/doc/aov.R
/usr/lib64/R/library/rstanarm/doc/aov.Rmd
/usr/lib64/R/library/rstanarm/doc/aov.html
/usr/lib64/R/library/rstanarm/doc/betareg.R
/usr/lib64/R/library/rstanarm/doc/betareg.Rmd
/usr/lib64/R/library/rstanarm/doc/betareg.html
/usr/lib64/R/library/rstanarm/doc/binomial.R
/usr/lib64/R/library/rstanarm/doc/binomial.Rmd
/usr/lib64/R/library/rstanarm/doc/binomial.html
/usr/lib64/R/library/rstanarm/doc/children/SETTINGS-gg.txt
/usr/lib64/R/library/rstanarm/doc/children/SETTINGS-knitr.txt
/usr/lib64/R/library/rstanarm/doc/children/SETTINGS-loo.txt
/usr/lib64/R/library/rstanarm/doc/children/SETTINGS-rstan.txt
/usr/lib64/R/library/rstanarm/doc/children/four_steps.txt
/usr/lib64/R/library/rstanarm/doc/children/stan_glm_priors.txt
/usr/lib64/R/library/rstanarm/doc/continuous.R
/usr/lib64/R/library/rstanarm/doc/continuous.Rmd
/usr/lib64/R/library/rstanarm/doc/continuous.html
/usr/lib64/R/library/rstanarm/doc/count.R
/usr/lib64/R/library/rstanarm/doc/count.Rmd
/usr/lib64/R/library/rstanarm/doc/count.html
/usr/lib64/R/library/rstanarm/doc/glmer.R
/usr/lib64/R/library/rstanarm/doc/glmer.Rmd
/usr/lib64/R/library/rstanarm/doc/glmer.html
/usr/lib64/R/library/rstanarm/doc/index.html
/usr/lib64/R/library/rstanarm/doc/jm.R
/usr/lib64/R/library/rstanarm/doc/jm.Rmd
/usr/lib64/R/library/rstanarm/doc/jm.html
/usr/lib64/R/library/rstanarm/doc/lm.R
/usr/lib64/R/library/rstanarm/doc/lm.Rmd
/usr/lib64/R/library/rstanarm/doc/lm.html
/usr/lib64/R/library/rstanarm/doc/polr.R
/usr/lib64/R/library/rstanarm/doc/polr.Rmd
/usr/lib64/R/library/rstanarm/doc/polr.html
/usr/lib64/R/library/rstanarm/doc/pooling.R
/usr/lib64/R/library/rstanarm/doc/pooling.Rmd
/usr/lib64/R/library/rstanarm/doc/pooling.html
/usr/lib64/R/library/rstanarm/doc/priors.R
/usr/lib64/R/library/rstanarm/doc/priors.Rmd
/usr/lib64/R/library/rstanarm/doc/priors.html
/usr/lib64/R/library/rstanarm/doc/rstanarm.R
/usr/lib64/R/library/rstanarm/doc/rstanarm.Rmd
/usr/lib64/R/library/rstanarm/doc/rstanarm.html
/usr/lib64/R/library/rstanarm/help/AnIndex
/usr/lib64/R/library/rstanarm/help/aliases.rds
/usr/lib64/R/library/rstanarm/help/figures/stanlogo.png
/usr/lib64/R/library/rstanarm/help/paths.rds
/usr/lib64/R/library/rstanarm/help/rstanarm.rdb
/usr/lib64/R/library/rstanarm/help/rstanarm.rdx
/usr/lib64/R/library/rstanarm/html/00Index.html
/usr/lib64/R/library/rstanarm/html/R.css
/usr/lib64/R/library/rstanarm/include/csr_matrix_times_vector2.hpp
/usr/lib64/R/library/rstanarm/include/meta_header.hpp
/usr/lib64/R/library/rstanarm/include/tests.cpp
/usr/lib64/R/library/rstanarm/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rstanarm/libs/rstanarm.so
/usr/lib64/R/library/rstanarm/libs/rstanarm.so.avx2
/usr/lib64/R/library/rstanarm/libs/rstanarm.so.avx512
