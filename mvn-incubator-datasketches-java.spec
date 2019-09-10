#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-incubator-datasketches-java
Version  : 0.9.0
Release  : 1
URL      : https://github.com/apache/incubator-datasketches-java/archive/sketches-0.9.0.tar.gz
Source0  : https://github.com/apache/incubator-datasketches-java/archive/sketches-0.9.0.tar.gz
Source1  : https://repo.maven.apache.org/maven2/com/yahoo/datasketches/sketches-core/0.9.0/sketches-core-0.9.0.jar
Source2  : https://repo.maven.apache.org/maven2/com/yahoo/datasketches/sketches-core/0.9.0/sketches-core-0.9.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-incubator-datasketches-java-data = %{version}-%{release}
Requires: mvn-incubator-datasketches-java-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
## Building sketches-core
Use Apache Maven 3.0 to build this project
### Requires JDK8
DataSketches sketches-core leverages new API methods introduced with JDK8.
JDK7 is no longer supported.

%package data
Summary: data components for the mvn-incubator-datasketches-java package.
Group: Data

%description data
data components for the mvn-incubator-datasketches-java package.


%package license
Summary: license components for the mvn-incubator-datasketches-java package.
Group: Default

%description license
license components for the mvn-incubator-datasketches-java package.


%prep
%setup -q -n incubator-datasketches-java-sketches-0.9.0

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-incubator-datasketches-java
cp LICENSE.md %{buildroot}/usr/share/package-licenses/mvn-incubator-datasketches-java/LICENSE.md
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/yahoo/datasketches/sketches-core/0.9.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/yahoo/datasketches/sketches-core/0.9.0/sketches-core-0.9.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/yahoo/datasketches/sketches-core/0.9.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/yahoo/datasketches/sketches-core/0.9.0/sketches-core-0.9.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/yahoo/datasketches/sketches-core/0.9.0/sketches-core-0.9.0.jar
/usr/share/java/.m2/repository/com/yahoo/datasketches/sketches-core/0.9.0/sketches-core-0.9.0.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-incubator-datasketches-java/LICENSE.md