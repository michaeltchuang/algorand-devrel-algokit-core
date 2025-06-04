import { toPascalCase, run } from "..";

export async function buildKotlin(crate: string) {
  let cargoBuildCmd = `cargo ndk --manifest-path crates/${crate}_ffi/Cargo.toml build`;

  await run(cargoBuildCmd);

  await run(
    `cargo --color always run -p uniffi-bindgen generate --no-format --library target/aarch64-linux-android/debug/lib${crate}_ffi.so --language kotlin --out-dir target/debug/kotlin/${crate}`,
  );
}
