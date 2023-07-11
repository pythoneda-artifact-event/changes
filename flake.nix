{
  description = "Events related to changes in source code";

  inputs = rec {
    nixos.url = "github:NixOS/nixpkgs/nixos-23.05";
    flake-utils.url = "github:numtide/flake-utils/v1.0.0";
    pythoneda-base = {
      url = "github:pythoneda/base/0.0.1a16";
      inputs.nixos.follows = "nixos";
      inputs.flake-utils.follows = "flake-utils";
    };
    pythoneda-artifact-shared-changes = {
      url = "github:pythoneda-artifact-shared/changes/0.0.1a1";
      inputs.nixos.follows = "nixos";
      inputs.flake-utils.follows = "flake-utils";
      inputs.pythoneda-base.follows = "pythoneda-base";
    };
  };
  outputs = inputs:
    with inputs;
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixos { inherit system; };
        pname = "pythoneda-artifact-event-changes";
        description = "Events related to changes in source code";
        license = pkgs.lib.licenses.gpl3;
        homepage = "https://github.com/pythoneda-artifact-event/changes";
        maintainers = with pkgs.lib.maintainers; [ ];
        nixpkgsRelease = "nixos-23.05";
        shared = import ./nix/shared.nix;
        pythonpackage = "pythonedaartifacteventchanges";
        pythoneda-artifact-event-changes-for = { version, pythoneda-base
          , pythoneda-artifact-shared-changes, python }:
          let
            pythonVersionParts = builtins.splitVersion python.version;
            pythonMajorVersion = builtins.head pythonVersionParts;
            pythonMajorMinorVersion =
              "${pythonMajorVersion}.${builtins.elemAt pythonVersionParts 1}";
            pnameWithUnderscores =
              builtins.replaceStrings [ "-" ] [ "_" ] pname;
            wheelName =
              "${pnameWithUnderscores}-${version}-py${pythonMajorVersion}-none-any.whl";
          in python.pkgs.buildPythonPackage rec {
            inherit pname version;
            projectDir = ./.;
            src = ./.;
            format = "pyproject";

            nativeBuildInputs = with python.pkgs; [ pip pkgs.jq poetry-core ];
            propagatedBuildInputs = with python.pkgs; [
              pythoneda-base
              pythoneda-artifact-shared-changes
            ];

            checkInputs = with python.pkgs; [ pytest ];

            pythonImportsCheck = [ pythonpackage ];

            preBuild = ''
              python -m venv .env
              source .env/bin/activate
              pip install ${pythoneda-base}/dist/pythoneda_base-${pythoneda-base.version}-py${pythonMajorVersion}-none-any.whl
              pip install ${pythoneda-artifact-shared-changes}/dist/pythoneda_artifact_shared_changes-${pythoneda-artifact-shared-changes.version}-py${pythonMajorVersion}-none-any.whl
              rm -rf .env
            '';

            postInstall = ''
              mkdir $out/dist
              ls dist/*
              cp dist/${wheelName} $out/dist
              jq ".url = \"$out/dist/${wheelName}\"" $out/lib/python${pythonMajorMinorVersion}/site-packages/${pnameWithUnderscores}-${version}.dist-info/direct_url.json > temp.json && mv temp.json $out/lib/python${pythonMajorMinorVersion}/site-packages/${pnameWithUnderscores}-${version}.dist-info/direct_url.json
            '';

            meta = with pkgs.lib; {
              inherit description homepage license maintainers;
            };
          };
        pythoneda-artifact-event-changes-0_0_1a1-for =
          { pythoneda-base, pythoneda-artifact-shared-changes, python }:
          pythoneda-artifact-event-changes-for {
            version = "0.0.1a1";
            inherit pythoneda-base pythoneda-artifact-shared-changes python;
          };
      in rec {
        packages = rec {
          pythoneda-artifact-event-changes-0_0_1a1-python38 =
            pythoneda-artifact-event-changes-0_0_1a1-for {
              pythoneda-base =
                pythoneda-base.packages.${system}.pythoneda-base-latest-python38;
              pythoneda-artifact-shared-changes =
                pythoneda-artifact-shared-changes.packages.${system}.pythoneda-artifact-shared-changes-latest-python38;
              python = pkgs.python38;
            };
          pythoneda-artifact-event-changes-0_0_1a1-python39 =
            pythoneda-artifact-event-changes-0_0_1a1-for {
              pythoneda-base =
                pythoneda-base.packages.${system}.pythoneda-base-latest-python39;
              pythoneda-artifact-shared-changes =
                pythoneda-artifact-shared-changes.packages.${system}.pythoneda-artifact-shared-changes-latest-python39;
              python = pkgs.python39;
            };
          pythoneda-artifact-event-changes-0_0_1a1-python310 =
            pythoneda-artifact-event-changes-0_0_1a1-for {
              pythoneda-base =
                pythoneda-base.packages.${system}.pythoneda-base-latest-python310;
              pythoneda-artifact-shared-changes =
                pythoneda-artifact-shared-changes.packages.${system}.pythoneda-artifact-shared-changes-latest-python310;
              python = pkgs.python310;
            };
          pythoneda-artifact-event-changes-latest-python38 =
            pythoneda-artifact-event-changes-0_0_1a1-python38;
          pythoneda-artifact-event-changes-latest-python39 =
            pythoneda-artifact-event-changes-0_0_1a1-python39;
          pythoneda-artifact-event-changes-latest-python310 =
            pythoneda-artifact-event-changes-0_0_1a1-python310;
          pythoneda-artifact-event-changes-latest =
            pythoneda-artifact-event-changes-latest-python310;
          default = pythoneda-artifact-event-changes-latest;
        };
        defaultPackage = packages.default;
        devShells = rec {
          pythoneda-artifact-event-changes-0_0_1a1-python38 =
            shared.devShell-for {
              package =
                packages.pythoneda-artifact-event-changes-0_0_1a1-python38;
              pythoneda-base =
                pythoneda-base.packages.${system}.pythoneda-base-latest-python38;
              python = pkgs.python38;
              inherit pkgs nixpkgsRelease;
            };
          pythoneda-artifact-event-changes-0_0_1a1-python39 =
            shared.devShell-for {
              package =
                packages.pythoneda-artifact-event-changes-0_0_1a1-python39;
              pythoneda-base =
                pythoneda-base.packages.${system}.pythoneda-base-latest-python39;
              python = pkgs.python39;
              inherit pkgs nixpkgsRelease;
            };
          pythoneda-artifact-event-changes-0_0_1a1-python310 =
            shared.devShell-for {
              package =
                packages.pythoneda-artifact-event-changes-0_0_1a1-python310;
              pythoneda-base =
                pythoneda-base.packages.${system}.pythoneda-base-latest-python310;
              python = pkgs.python310;
              inherit pkgs nixpkgsRelease;
            };
          pythoneda-artifact-event-changes-latest-python38 =
            pythoneda-artifact-event-changes-0_0_1a1-python38;
          pythoneda-artifact-event-changes-latest-python39 =
            pythoneda-artifact-event-changes-0_0_1a1-python39;
          pythoneda-artifact-event-changes-latest-python310 =
            pythoneda-artifact-event-changes-0_0_1a1-python310;
          pythoneda-artifact-event-changes-latest =
            pythoneda-artifact-event-changes-latest-python310;
          default = pythoneda-artifact-event-changes-latest;

        };
      });
}
