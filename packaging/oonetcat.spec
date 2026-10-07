Name:           oonetcat
Version:        0.1.0
Release:        1%{?dist}
Summary:        Capability-isolated socket communicator for port inspection and raw byte exchange.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oonetcat
Source0:        oonetcat-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oonetcat is a sovereign, capability-bounded RAW TCP/UDP written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oonetcat
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oonetcat-uninstall

%files
/usr/bin/oonetcat
/usr/bin/oonetcat-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
