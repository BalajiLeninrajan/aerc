# RPM for the balaji fork of aerc, built by .github/workflows/fedora.yml.
# The workflow passes ver (0.22.0), rel (<run number>.git<sha>) and
# fullver (git describe output, shown by aerc -v).

# make does not pass a Go build-id, so skip the debuginfo subpackage
%global debug_package %{nil}

Name:           aerc
Version:        %{ver}
Release:        %{rel}%{?dist}
Summary:        Email client for your terminal (balaji fork)
License:        MIT
URL:            https://github.com/BalajiLeninrajan/aerc
Source0:        aerc.tar.gz

BuildRequires:  diffutils
BuildRequires:  gcc
BuildRequires:  golang
BuildRequires:  make
BuildRequires:  notmuch-devel
BuildRequires:  scdoc
Requires:       w3m
# img2sixel, for inline images with the html filter's -sixel option
Requires:       libsixel-utils

%description
aerc, the terminal email client, with the fork's patches: the embedded
terminal knows its size in pixels, so sixel images from filters such as
w3m -sixel display instead of scrolling the text away.

%prep
%autosetup -n aerc

%build
make PREFIX=%{_prefix} VERSION=%{fullver} GOFLAGS=-tags=notmuch

%install
make install PREFIX=%{_prefix} DESTDIR=%{buildroot} VERSION=%{fullver} GOFLAGS=-tags=notmuch

%files
%license LICENSE
%{_bindir}/aerc
%{_bindir}/carddav-query
%{_libexecdir}/aerc/
%{_datadir}/aerc/
%{_datadir}/applications/aerc.desktop
%{_datadir}/icons/hicolor/scalable/apps/aerc.svg
%{_mandir}/man1/aerc*
%{_mandir}/man1/carddav-query*
%{_mandir}/man5/aerc*
%{_mandir}/man7/aerc*
