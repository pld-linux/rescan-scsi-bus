Summary:	Rescan SCSI bus in Linux
Name:		rescan-scsi-bus
Version:	1.24
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.garloff.de/kurt/linux/%{name}.sh
# Source0-md5:	4dad7c30e1e61defd2fb38a84087c013
URL:		http://www.garloff.de/kurt/linux/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux allows you to add and remove SCSI devices without rebooting by
using the echo "scsi add-single-device H C I L" > /proc/scsi/scsi
command (H = host, C = channel, I = SCSI ID, L = SCSI LUN). The
remove-single-device command works similarily.

Note, however, that the SCSI bus was NOT designed for hot-plugging, so
you might be out of luck ... And you have to be sure, that termination
is OK. All filesystems on a device have to be unmounted before
disconnecting it or powering it down.

%prep
%setup -q -c -T
install %{SOURCE0} %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install %{name} $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/rescan-scsi-bus
