# rpm-build

[![License](https://img.shields.io/badge/license-GPLv3-brightgreen.svg?style=flat)](COPYING)

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

## License

Copyright (C) 2023 Linux HeadQuarters

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
