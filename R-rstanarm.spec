#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rstanarm
Version  : 2.18.2
Release  : 23
URL      : https://cran.r-project.org/src/contrib/rstanarm_2.18.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rstanarm_2.18.2.tar.gz
Summary  : Bayesian Applied Regression Modeling via Stan
Group    : Development/Tools
License  : GPL-3.0
Requires: R-rstanarm-lib = %{version}-%{release}
Requires: R-minqa
Requires: R-nloptr
Requires: R-reshape2
Requires: R-rsconnect
BuildRequires : R-BH
BuildRequires : R-DT
BuildRequires : R-Rcpp
BuildRequires : R-RcppEigen
BuildRequires : R-StanHeaders
BuildRequires : R-base64enc
BuildRequires : R-bayesplot
BuildRequires : R-betareg
BuildRequires : R-biglm
BuildRequires : R-callr
BuildRequires : R-colourpicker
BuildRequires : R-crosstalk
BuildRequires : R-dplyr
BuildRequires : R-dygraphs
BuildRequires : R-gamm4
BuildRequires : R-ggridges
BuildRequires : R-gridExtra
BuildRequires : R-gtable
BuildRequires : R-gtools
BuildRequires : R-htmlwidgets
BuildRequires : R-igraph
BuildRequires : R-inline
BuildRequires : R-lazyeval
BuildRequires : R-lme4
BuildRequires : R-loo
BuildRequires : R-mime
BuildRequires : R-minqa
BuildRequires : R-munsell
BuildRequires : R-nloptr
BuildRequires : R-pillar
BuildRequires : R-pkgbuild
BuildRequires : R-pkgconfig
BuildRequires : R-plyr
BuildRequires : R-prettyunits
BuildRequires : R-ps
BuildRequires : R-purrr
BuildRequires : R-reshape2
BuildRequires : R-rlang
BuildRequires : R-roxygen2
BuildRequires : R-rsconnect
BuildRequires : R-rstan
BuildRequires : R-rstantools
BuildRequires : R-scales
BuildRequires : R-shinystan
BuildRequires : R-shinythemes
BuildRequires : R-threejs
BuildRequires : R-tibble
BuildRequires : R-xts
BuildRequires : R-yaml
BuildRequires : R-zoo
BuildRequires : buildreq-R

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
export SOURCE_DATE_EPOCH=1552947751

%install
export SOURCE_DATE_EPOCH=1552947751
rm -rf %{buildroot}
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
R CMD check --no-manual --no-examples --no-codoc  rstanarm || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rstanarm/CITATION
/usr/lib64/R/library/rstanarm/DESCRIPTION
/usr/lib64/R/library/rstanarm/INDEX
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
/usr/lib64/R/library/rstanarm/NEWS.md
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
/usr/lib64/R/library/rstanarm/tests/testthat.R
/usr/lib64/R/library/rstanarm/tests/testthat/Rplots.pdf
/usr/lib64/R/library/rstanarm/tests/testthat/helpers/SW.R
/usr/lib64/R/library/rstanarm/tests/testthat/helpers/check_for_error.R
/usr/lib64/R/library/rstanarm/tests/testthat/helpers/expect_equivalent_loo.R
/usr/lib64/R/library/rstanarm/tests/testthat/helpers/expect_gg.R
/usr/lib64/R/library/rstanarm/tests/testthat/helpers/expect_identical_sorted_stanmats.R
/usr/lib64/R/library/rstanarm/tests/testthat/helpers/expect_linpred_equal.R
/usr/lib64/R/library/rstanarm/tests/testthat/helpers/expect_matrix.R
/usr/lib64/R/library/rstanarm/tests/testthat/helpers/expect_ppd.R
/usr/lib64/R/library/rstanarm/tests/testthat/helpers/expect_stanmvreg.R
/usr/lib64/R/library/rstanarm/tests/testthat/helpers/expect_stanreg.R
/usr/lib64/R/library/rstanarm/tests/testthat/helpers/expect_survfit.R
/usr/lib64/R/library/rstanarm/tests/testthat/helpers/get_tols.R
/usr/lib64/R/library/rstanarm/tests/testthat/helpers/recover_pars.R
/usr/lib64/R/library/rstanarm/tests/testthat/include/csr_matrix_times_vector2.hpp
/usr/lib64/R/library/rstanarm/tests/testthat/include/meta_header.hpp
/usr/lib64/R/library/rstanarm/tests/testthat/include/tests.cpp
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/bernoulli.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/binomial.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/continuous.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/count.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/data/NKX.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/data/data_assoc.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/data/data_betareg.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/data/data_event.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/data/data_glm.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/data/data_mvmer.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/data/dimensions_mvmer.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/data/glmer_stuff.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/data/glmer_stuff2.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/data/hyperparameters.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/data/hyperparameters_assoc.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/data/hyperparameters_event.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/data/hyperparameters_mvmer.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/data/weights_offset.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/functions/SSfunctions.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/functions/bernoulli_likelihoods.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/functions/binomial_likelihoods.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/functions/common_functions.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/functions/continuous_likelihoods.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/functions/count_likelihoods.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/functions/jm_functions.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/functions/mvmer_functions.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/gqs/gen_quantities_mvmer.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/jm.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/lm.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/model/assoc_evaluate.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/model/eta_add_Zb.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/model/eta_no_intercept.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/model/eta_z_no_intercept.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/model/event_lp.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/model/make_eta.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/model/make_eta_bern.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/model/make_eta_tmp.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/model/make_eta_tmp2.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/model/make_eta_z.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/model/mvmer_lp.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/model/priors_betareg.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/model/priors_glm.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/model/priors_mvmer.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/mvmer.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/parameters/parameters_assoc.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/parameters/parameters_betareg.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/parameters/parameters_event.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/parameters/parameters_glm.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/parameters/parameters_mvmer.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/polr.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/pre/Brilleman_copyright.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/pre/Columbia_copyright.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/pre/license.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/tdata/tdata_betareg.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/tdata/tdata_glm.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/tdata/tdata_mvmer.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/tparameters/tparameters_betareg.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/tparameters/tparameters_glm.stan
/usr/lib64/R/library/rstanarm/tests/testthat/stan_files/tparameters/tparameters_mvmer.stan
/usr/lib64/R/library/rstanarm/tests/testthat/test_loo.R
/usr/lib64/R/library/rstanarm/tests/testthat/test_methods.R
/usr/lib64/R/library/rstanarm/tests/testthat/test_misc.R
/usr/lib64/R/library/rstanarm/tests/testthat/test_plots.R
/usr/lib64/R/library/rstanarm/tests/testthat/test_posterior_predict.R
/usr/lib64/R/library/rstanarm/tests/testthat/test_pp_check.R
/usr/lib64/R/library/rstanarm/tests/testthat/test_pp_validate.R
/usr/lib64/R/library/rstanarm/tests/testthat/test_predict.R
/usr/lib64/R/library/rstanarm/tests/testthat/test_stan_betareg.R
/usr/lib64/R/library/rstanarm/tests/testthat/test_stan_clogit.R
/usr/lib64/R/library/rstanarm/tests/testthat/test_stan_functions.R
/usr/lib64/R/library/rstanarm/tests/testthat/test_stan_glm.R
/usr/lib64/R/library/rstanarm/tests/testthat/test_stan_glmer.R
/usr/lib64/R/library/rstanarm/tests/testthat/test_stan_jm.R
/usr/lib64/R/library/rstanarm/tests/testthat/test_stan_lm.R
/usr/lib64/R/library/rstanarm/tests/testthat/test_stan_mvmer.R
/usr/lib64/R/library/rstanarm/tests/testthat/test_stan_nlmer.R
/usr/lib64/R/library/rstanarm/tests/testthat/test_stan_polr.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rstanarm/libs/rstanarm.so
