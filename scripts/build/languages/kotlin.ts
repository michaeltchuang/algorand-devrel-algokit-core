import { toPascalCase, run } from "..";

export async function buildKotlin(crate: string) {
  const targets = [
    // "aarch64-linux-android"
  ];

  let cargoBuildCmd = `cargo --color always build --manifest-path crates/${crate}_ffi/Cargo.toml`;

  targets.map((target) => {
    cargoBuildCmd += ` --target ${target}`;
  });

  await run(cargoBuildCmd);

  await run(
    `cargo --color always run -p uniffi-bindgen generate --no-format --library target/debug/lib${crate}_ffi.dylib --language kotlin --out-dir target/debug/kotlin/${crate}`,
  );
}
