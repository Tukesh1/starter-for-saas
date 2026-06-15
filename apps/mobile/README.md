# FLIPO-SAAS – Mobile App (Optional)

This is the mobile companion app for FLIPO-SAAS, built with **Expo + React Native**. Ideal for users who need quick access to core features on the go.

## 📦 Tech Stack
- [React Native](https://reactnative.dev/)
- [Expo](https://expo.dev/)
- [TypeScript](https://www.typescriptlang.org/)
- [Supabase JS](https://supabase.com/docs/reference/javascript)

## 🚀 Getting Started

```bash
cd apps/mobile
pnpm install
npx expo start
````

## 🧱 Features

* Supabase authentication
* Minimal dashboard UI
* Notifications (expo-notifications)

## 🔐 Auth

Uses Supabase client session tokens via mobile SDK.

## 📁 Structure

```
src/
 ├─ screens/
 ├─ components/
 ├─ hooks/
 └─ App.tsx
```

> ⚠️ Note: This app is optional for MVP and can be added later.



