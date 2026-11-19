# Church Analytics App

Church analytics app (English first; Spanish planned for later) for pastors: attendance, giving, and social media stats. Web dashboard + mobile app on one Django API.

See @ARCHITECTURE.md for the full stack and diagram.

## Key rules

- Every tenant-owned table has a `church_id`; never return data across churches. Tests must check that Church A can't see Church B's data.
- Giving data is visible only to financial roles; other staff see aggregates.
- Record donations only (manual entry or CSV import). Never process payments.
- English only for now; don't add Spanish translations yet. Still wrap user-facing text for i18n (`en.json` on the frontends, `gettext` on the backend) so Spanish can be added later without rewrites.
- Encrypt stored OAuth tokens for social accounts.

## Repo layout

- `backend/`: Django + Django Ninja, PostgreSQL, Celery + Redis
- `web/`: React + TypeScript + Vite
- `mobile/`: Expo + React Native
- `packages/shared/`: generated API client, Zod schemas, translations

## Dev environment

- Windows + PowerShell. Activate the venv with `.venv\Scripts\Activate.ps1` and use `python -m ...` inside it.
- Local services run with Docker Compose.
