Summary:	Rescan SCSI bus in Linux
Summary(pl.UTF-8):	Ponowne skanowanie szyny SCSI pod Linuksem
Name:		rescan-scsi-bus
Version:	1.56
Release:	1
License:	GPL v2 or GPL v3
Group:		Applications/System
# http://www.garloff.de/kurt/linux/rescan-scsi-bus.sh (with changed CVS tag)
Source0:	%{name}.sh
URL:		http://www.garloff.de/kurt/linux/#rescan-scsi
Requires:	sg3_utils
Obsoletes:	scsiutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux allows you to add and remove SCSI devices without rebooting by
using the

echo "scsi add-single-device H C I L" > /proc/scsi/scsi

command (H = host, C = channel, I = SCSI ID, L = SCSI LUN). The
remove-single-device command works similarily.

Note, however, that the SCSI bus was NOT designed for hot-plugging, so
you might be out of luck... And you have to be sure, that termination
is OK. All filesystems on a device have to be unmounted before
disconnecting it or powering it down.

%description -l pl.UTF-8
Linux pozwala dodawać i usuwać urządzenia SCSI bez rebootowania
systemu za pomocą polecenia

echo "scsi add-single-device H C I L" > /proc/scsi/scsi

(H = host, C = kanał, I = SCSI ID, L = SCSI LUN). Polecenie
remove-single-device działa podobnie.

Jednak należy zauważyć, że szyna SCSI nie została zaprojektowana do
podłączania urządzeń w locie, więc można mieć pecha... Dodatkowo
trzeba być pewnym, że terminacja jest prawidłowa. Wszystkie systemy
plików na urządzeniu muszą być odmontowane przed jego odłączeniem lub
wyłączeniem.

%prep
%setup -qcT
install -p %{SOURCE0} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install -p %{name}.sh $RPM_BUILD_ROOT%{_sbindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/rescan-scsi-bus
