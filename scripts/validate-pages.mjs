/**
 * Run the same HTML linter locally and in CI: node scripts/validate-pages.mjs.
 * npm owns its normal package cache; this command creates no repository output.
 * Only these public documents are read. No account or application data is used.
 */
import { execSync } from "node:child_process";
import { fileURLToPath } from "node:url";

try {
  // A fixed command works with npm's Windows shim and accepts no user input.
  execSync(
    "npx --yes --package html-validate@11.14.0 html-validate docs/index.html docs/privacy.html",
    {
      cwd: fileURLToPath(new URL("../", import.meta.url)),
      stdio: "inherit",
      windowsHide: true,
    },
  );
} catch (error) {
  process.exit(error.status || 1);
}
console.log("OK");
