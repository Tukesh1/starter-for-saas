# FLIPO-SAAS – Web App

This is the main user-facing frontend for FLIPO-SAAS. Built with **Next.js 14 (App Router)** and **Tailwind CSS**, it serves as the core dashboard for SaaS users.

## 📦 Tech Stack
- [Next.js 14+](https://nextjs.org/)
- [TypeScript](https://www.typescriptlang.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [PNPM Workspaces](https://pnpm.io/)
- [Supabase Auth](https://supabase.com/)

## 🚀 Getting Started

```bash
cd apps/web
pnpm install
pnpm dev
````

## 🌐 Environment Variables

Create a `.env.local` file:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🧱 Features

* Supabase Auth integration
* Dashboard pages (based on user plan)
* Responsive design
* API connection to FastAPI backend

## 🛠 Commands

| Command      | Description      |
| ------------ | ---------------- |
| `pnpm dev`   | Start dev server |
| `pnpm build` | Build for prod   |
| `pnpm lint`  | Lint codebase    |

## 📁 Project Structure

```
app/
 ├─ layout.tsx
 ├─ page.tsx
 └─ dashboard/
       ├─ page.tsx
       └─ components/
```
