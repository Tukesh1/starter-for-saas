# FLIPO-SAAS – Admin Dashboard

This is the internal admin interface used to manage users, billing, service logs, and system configurations.

## 📦 Tech Stack
- [Next.js](https://nextjs.org/)
- [TypeScript](https://www.typescriptlang.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [ShadCN UI](https://ui.shadcn.dev/) (optional)

## 🚀 Getting Started

```bash
cd apps/admin
pnpm install
pnpm dev
````

## 🧱 Features

* View/manage users
* Webhook logs
* Billing overview
* App status monitors

## 🔐 Auth

This app is typically protected by:

* Supabase admin check or
* Role-based token auth (JWT)

## 🌐 Environment Variables

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🛠 Commands

| Command      | Description      |
| ------------ | ---------------- |
| `pnpm dev`   | Start dev server |
| `pnpm build` | Build for prod   |
| `pnpm lint`  | Lint codebase    |

