#python -m streamlit run WEB.py
import streamlit as st

#image download
def image_download(ddr):
    addr ="image/" + ddr
    with open(addr, "rb") as file:
        btn = st.download_button(
                label="Download image",
                data=file,
                file_name="download.jpg",
                mime="image/jpg")

#videoplay
def videoplay(ddr):
    addr = "video/" + ddr
    video_file = open(addr, "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)

#imageshow
def showpic(ddr):
    addr = "image/" + ddr
    image_file = open(addr, "rb")
    image_bytes = image_file.read()
    st.image(image_bytes, caption="Here's an image:")


#Subject selection
def choosesub():
    if "selected_subject" not in st.session_state:
        st.session_state.selected_subject = None

    selected_subject = st.selectbox("Choose a subject", ["Math", "Science", "History", "English"])
    st.session_state.selected_subject = selected_subject

    if st.session_state.selected_subject == "Math":
        st.write("You have selected Math. Here is some Math content:")
        # Display Math content
        showpic("20240603082006.jpg")
    elif st.session_state.selected_subject == "Science":
        st.write("You have selected Science. Here is some Science content:")
        # Display Science content
    elif st.session_state.selected_subject == "History":
        st.write("You have selected History. Here is some History content:")
        # Display History content
    elif st.session_state.selected_subject == "English":
        st.write("You have selected English. Here is some English content:")
        # Display English content





def main():
    st.title("AAA App")
    st.sidebar.title("wawawa")
    choice = st.sidebar.radio("笔记资料", ["讲解视频", "竞赛资料", "试卷解析"])

    if choice == "讲解视频":
        st.subheader("Welcome to the Home Page!")
        st.write("This is the content for the home page.")
        choosesub()
    elif choice == "竞赛资料":
        st.subheader("This is Page 1")
        st.write("This is the content for Page 1.")
        image_download("20240603082006.jpg")
    elif choice == "试卷解析":
        st.subheader("This is Page 2")
        st.write("This is the content for Page 2.")
        videoplay("3.mp4")


if __name__ == "__main__":
    main()