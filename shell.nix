{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell rec {
    buildInputs = with pkgs; [
        python312
        python312Packages.pip
        python312Packages.virtualenvwrapper
        #python312Packages.pyside6
        python312Packages.drawsvg # https://pypi.org/project/drawsvg/
    ];

    shellHook = ''
        export TMPDIR=/tmp  && export VENV=$(mktemp -d)
        virtualenv --system-site-packages $VENV
        source $VENV/bin/activate
        pip install mingus # https://bspaans.github.io/python-mingus/doc/wiki/tutorialNoteModule.html
    '';
}
