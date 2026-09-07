# Docs-and-Claims public information

Public homepage and Gmail privacy notice for Docs-and-Claims.
The application is not distributed in this repository.

GitHub Pages serves the static files in `docs/` from `main`.
No installation or build step is required. The privacy notice's canonical
source is `docs/privacy.html`.

Validate locally and in CI with Python 3.10+ and Node.js 24:
`python scripts/validate-repository.py --evidence-file PATH`.
Choose an evidence path outside the checkout and remove it after inspection.
The repository validator delegates the two HTML documents to
`scripts/validate-pages.mjs`, using the pinned HTML validator through npm's
normal cache. It does not build or run the private application.

The notice uses original wording, informed by these personal-application examples:

- [Calendar.Express](https://calendar.express/privacy)
- [Maisie](https://maisieai.online/privacy)
- [Ethan Flynn CRM](https://ethanflynn.com/privacy)

These references are not affiliations or evidence of Google approval.
