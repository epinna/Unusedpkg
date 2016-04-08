%define name 		unusedpkg
%define Summary		Diagnostic tool to find unused packages
%define sourcetype      tar.gz
%define version         1.0

Name:         %name
Summary:       %Summary
Version:       %version
Release:       %mkrel 1
License:       GPL3
Distribution: blackPanther OS
Vendor:       blackPanther Europe
Packager:     Miklos Horvath
Group:        Tools
Source0:      %name-%version.%sourcetype
Buildroot:     %_tmppath/%name-%version-%release-root

%description
UnusedPkg is a diagnostic tool to find the unused
packages in your Linux system, sorted by their 
idle time. This helps to find unused packages 
which could be manually removed to free some 
space in the filesystem. It supports any
apt-based distribution (tested on Debian and 
Ubuntu), Slackware and blackPanther OS.

By default UnusedPkg collect the timestamps of 
the packages having binaries installed in the 
$PATH folders.
Use `-a` option to collect the statistics of 
every package installed in the system.

%files
%defattr(-,root,root)
%_bindir/
%_datadir/

%prep
%setup -q 

%build
# We don't need to build

%install
mkdir -p %buildroot/%_bindir 
mkdir -p %buildroot/%_datadir
bash install.sh -b %buildroot/%_bindir -d %buildroot/%_datadir

%clean
rm -rf %buildroot


%changelog
* Fri Apr 08 2016 Miklos Horvath <hmiki@blackpantheros.eu> 
- initial version
