import { toPascalCase, run } from "..";

export async function buildKotlin(crate: string) {
    const soFileOutputDir = "packages/android/algokit_transact/transact/src/main/jniLibs";
    const kotlinOutDir = "packages/android/algokit_transact/transact/src/main/kotlin";

    let cargoBuildCmd = `cargo ndk -o ${soFileOutputDir} \
       --manifest-path crates/${crate}_ffi/Cargo.toml \
       -t armeabi-v7a \
       -t arm64-v8a \
       -t x86_64 \
       build --release`;

    await run(cargoBuildCmd);

    const libraryPath = `target/aarch64-linux-android/release/lib${crate}_ffi.so`;
    await run(
        `cargo run -p uniffi-bindgen generate \
        --library ${libraryPath} \
        --language kotlin \
        --out-dir ${kotlinOutDir}`
      );
}
