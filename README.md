# rpm-build

[![License](https://img.shields.io/badge/license-GPLv3-lightgreen)](https://www.gnu.org/licenses/gpl-3.0.en.html#license-text)

A collection of rpm specs and sources

# Build

## Dependencies

    sudo yum -y install mock rpmdevtools
    sudo usermod -a -G mock $(whoami)

## Working environment

    source /etc/os-release
    PACKAGE=hatop

## Clone repository

    tmp=$(mktemp -d)
    git clone https://github.com/linuxhq/rpm-build.git ${tmp}
    mkdir -p ${tmp}/${PACKAGE}/{SOURCES,SRPMS}

## Build package

    spectool -g -C \
             ${tmp}/${PACKAGE}/SOURCES \
             ${tmp}/${PACKAGE}/SPECS/*.spec

    mock --clean \
         --root epel-${VERSION_ID}-$(uname -i)

    mock --buildsrpm \
         --cleanup-after \
         --resultdir ${tmp}/${PACKAGE}/SRPMS \
         --root epel-${VERSION_ID}-$(uname -i) \
         --sources ${tmp}/${PACKAGE}/SOURCES \
         --spec ${tmp}/${PACKAGE}/SPECS/*.spec

    mock --rebuild \
         --root epel-${VERSION_ID}-$(uname -i) \
         ${tmp}/${PACKAGE}/SRPMS/*.src.rpm

    rm -rf ${tmp}
