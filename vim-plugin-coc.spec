%define		plugin coc
Summary:	Vim plugin: Intellisense engine, full language server protocol support as VSCode
Name:		vim-plugin-%{plugin}
Version:	0.0.82
Release:	1
License:	MIT
Group:		Applications/Editors/Vim
Source0:	https://github.com/neoclide/coc.nvim/archive/v%{version}/coc.nvim-%{version}.tar.gz
# Source0-md5:	f9168183528e26947ad42ef302bf2769
URL:		https://github.com/neoclide/coc.nvim/
Requires:	nodejs >= 10.12
Requires:	vim-rt >= 4:8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
Coc.nvim enhances your (Neo)Vim to match the user experience provided
by VSCode through rich plugin ecosystem and Language Server Protocol
support.

Some of the features include:
- APIs that are compatible with both Vim (>= 8.0) and Neovim.
- Loading VSCode-like extensions.
- Configuring coc.nvim and its extensions by using JSON configuration
  file.
- Configuring Language Servers that implement Language Server Protocol
  (LSP).

%package doc
Summary:	Documentation for coc Vim plugin
Requires(post,postun):	/usr/bin/vim
Requires:	%{name} = %{version}-%{release}
Requires:	vim-rt >= 4:7.4.2054-2

%description doc
Documentation for coc Vim plugin.

%prep
%setup -qn coc.nvim-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/{pack/coc/start/coc.nvim,doc}
cp -pr autoload bin build data plugin package.json $RPM_BUILD_ROOT%{_vimdatadir}/pack/coc/start/coc.nvim
cp -p doc/coc.* $RPM_BUILD_ROOT%{_vimdatadir}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%post doc
%vim_doc_helptags

%postun doc
%vim_doc_helptags

%files
%defattr(644,root,root,755)
%doc Readme.md history.md
%dir %{_vimdatadir}/pack/coc
%dir %{_vimdatadir}/pack/coc/start
%dir %{_vimdatadir}/pack/coc/start/coc.nvim
%{_vimdatadir}/pack/coc/start/coc.nvim/autoload
%dir %{_vimdatadir}/pack/coc/start/coc.nvim/bin
%attr(755,root,root) %{_vimdatadir}/pack/coc/start/coc.nvim/bin/prompt.js
%attr(755,root,root) %{_vimdatadir}/pack/coc/start/coc.nvim/bin/terminateProcess.sh
%{_vimdatadir}/pack/coc/start/coc.nvim/build
%{_vimdatadir}/pack/coc/start/coc.nvim/data
%{_vimdatadir}/pack/coc/start/coc.nvim/plugin
%{_vimdatadir}/pack/coc/start/coc.nvim/package.json

%files doc
%defattr(644,root,root,755)
%{_vimdatadir}/doc/coc.*
