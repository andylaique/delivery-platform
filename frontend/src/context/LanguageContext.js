import { createContext, useContext, useState, useEffect, useCallback } from "react";
import { t as translate, LOCALES } from "@/lib/i18n";

const LanguageContext = createContext(null);

const STORAGE_KEY = "dp_locale";

export function LanguageProvider({ children }) {
  const [locale, setLocaleState] = useState("en");

  useEffect(() => {
    if (typeof window === "undefined") return;
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved && LOCALES.some((l) => l.code === saved)) {
      setLocaleState(saved);
    }
  }, []);

  const setLocale = useCallback((code) => {
    if (!LOCALES.some((l) => l.code === code)) return;
    setLocaleState(code);
    if (typeof window !== "undefined") {
      localStorage.setItem(STORAGE_KEY, code);
      document.documentElement.lang = code === "rw" ? "rw" : code;
    }
  }, []);

  const t = useCallback((key) => translate(locale, key), [locale]);

  return (
    <LanguageContext.Provider value={{ locale, setLocale, t, locales: LOCALES }}>
      {children}
    </LanguageContext.Provider>
  );
}

export function useLanguage() {
  const ctx = useContext(LanguageContext);
  if (!ctx) throw new Error("useLanguage must be used inside LanguageProvider");
  return ctx;
}
