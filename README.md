# Source code events

This package declares the events relevant to changes in the source code.

## How to declare it in your flake

Check the latest tag of the artifact repository: https://github.com/pythoneda-shared-artifact/events-artifact/tags, and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-shared-artifact-events = {
      [optional follows]
      url =
        "github:pythoneda-shared-artifact/events-artifact/[version]?dir=events";
    };
  };
  outputs = [..]
};
```

Should you use another PythonEDA modules, you might want to pin those also used by this project. The same applies to [https://nixos/nixpkgs](nixpkgs "nixpkgs") and [https://github.com/numtide/flake-utils](flake-utils "flake-utils").

The Nix flake is under the [https://github.com/pythoneda-shared-artifact/events-artifact/tree/main/events](events "events") folder of <https://github.com/pythoneda-shared-artifact/events-artifact>.

