import styles from "./Button.module.css";

export default function Button({
  children,
  variant = "primary",
  size = "md",
  fullWidth,
  className = "",
  ...props
}) {
  const cls = [
    styles.btn,
    styles[variant] || styles.primary,
    styles[size] || styles.md,
    fullWidth ? styles.full : "",
    className,
  ]
    .filter(Boolean)
    .join(" ");
  return (
    <button type="button" className={cls} {...props}>
      {children}
    </button>
  );
}
