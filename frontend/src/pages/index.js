import { useEffect } from "react";
import { useRouter } from "next/router";
import { useAuth } from "@/context/AuthContext";
import { useLanguage } from "@/context/LanguageContext";
import styles from "./index.module.css";

export default function Home() {
  const { user, loading } = useAuth();
  const { t } = useLanguage();
  const router = useRouter();

  useEffect(() => {
    if (loading) return;
    if (!user) {
      router.replace("/auth/login");
      return;
    }
    if (user.role === "manager") router.replace("/manager");
    else if (user.role === "vendor") router.replace("/vendor");
    else router.replace("/client");
  }, [user, loading, router]);

  return (
    <div className={styles.loading}>
      <div className={styles.spinner} />
      <p>{t("loadingPlatform")}</p>
    </div>
  );
}
