import "./styles/globals.css"
import type { Metadata } from "next";
export const metadata: Metadata = {
    title: "My App",
};
export default function Layout({ children }: { children: React.ReactNode }) {
    return (
        <html>
            <body>
                {children}
            </body>
        </html>
    )
}