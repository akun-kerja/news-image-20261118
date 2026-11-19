// News-image entry for 18 November 2026 (Node 22, standard library only).
// The image was drawn by build_image.py from verified news of that day
// and is stored beside this file as entry.png. This program copies it,
// byte for byte, to the grader's output directory, so both runs of the
// program write exactly the same file.
//
// Local run:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
if (!existsSync(source)) {
  throw new Error("entry.png is missing from the repository");
}
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
if (!existsSync(outDir)) {
  mkdirSync(outDir, { recursive: true });
}
copyFileSync(source, join(outDir, "entry.png"));
