import streamlit as st

def resources_page():
    st.set_page_config(page_title="📚 Resource Hub", layout="wide")

    st.title("📚 Resource Hub")
    st.write("A curated collection of learning resources for students from **all academic streams**.")

    st.markdown("---")

    # Commerce Section
    st.subheader("📈 Commerce")
    st.markdown("- [Accounting Basics](https://www.accountingcoach.com/) — Learn fundamentals of accounting.")
    st.markdown("- [Investopedia](https://www.investopedia.com/) — Finance, investing, and business guides.")
    st.markdown("- [Corporate Finance Institute](https://corporatefinanceinstitute.com/) — Professional finance courses.")

    st.markdown("---")

    # Science Section
    st.subheader("🧪 Science")
    st.markdown("- [Khan Academy Science](https://www.khanacademy.org/science) — Free science lessons & practice.")
    st.markdown("- [CrashCourse](https://www.youtube.com/user/crashcourse) — Fun, fast-paced educational videos.")
    st.markdown("- [NASA Science](https://science.nasa.gov/) — Space & science articles.")

    st.markdown("---")

    # Arts & Humanities Section
    st.subheader("🖋️ Arts & Humanities")
    st.markdown("- [Coursera Humanities](https://www.coursera.org/browse/arts-and-humanities) — Online university courses.")
    st.markdown("- [Open Yale Courses](https://oyc.yale.edu/) — Free lectures from Yale.")
    st.markdown("- [TED Talks](https://www.ted.com/topics/humanities) — Inspiring talks and ideas.")

    st.markdown("---")

    # Technology Section
    st.subheader("💻 Technology")
    st.markdown("- [FreeCodeCamp](https://www.freecodecamp.org/) — Learn coding and web development.")
    st.markdown("- [W3Schools](https://www.w3schools.com/) — Programming and web tutorials.")
    st.markdown("- [GeeksforGeeks](https://www.geeksforgeeks.org/) — Computer science concepts and coding practice.")

    st.markdown("---")

    st.success("💡 Tip: Bookmark this page so you can come back anytime for quick study resources!")

# Run standalone
if __name__ == "__main__":
    resources_page()
