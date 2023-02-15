from pytube import YouTube
import customtkinter as ctk
import tkinter.filedialog
from PIL import Image
import os

# Commands


def change_appearance_mode_event(new_appearance_mode: str):
    ctk.set_appearance_mode(new_appearance_mode)


def change_scaling_event(new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    ctk.set_widget_scaling(new_scaling_float)


def select_folder():
    folder_path = tkinter.filedialog.askdirectory()

    if location_list:
        location_list.pop(0)
    location_list.append(folder_path)
    element_from_location = location_list[0]
    str(element_from_location)

    if folder_path:
        file_path_description.configure(text=f"File location: {folder_path}", wraplength=300)
    else:
        file_path_description.configure(text="N/A")


def success():
    pop_up_1 = ctk.CTkToplevel()
    pop_up_1.geometry("300x300")
    pop_up_1.title("Download video")

    # Label
    description_1 = ctk.CTkLabel(
        master=pop_up_1, text="Your video has been successfully downloaded", font=font)
    description_1.grid(row=0, column=0, padx=10, pady=20)

    # Confirmation button
    confirmation_button_1 = ctk.CTkButton(
        master=pop_up_1, width=50, text="OK", corner_radius=5, command=lambda: quit_pop_up(pop_up=pop_up_1), fg_color="#541690", hover_color="#2c0e47")
    confirmation_button_1.grid(row=1, column=0, padx=125, pady=50)


def error():
    pop_up_3 = ctk.CTkToplevel()
    pop_up_3.geometry("300x300")
    pop_up_3.title("Error")

    # Label
    error_description_3 = ctk.CTkLabel(
        master=pop_up_3, text="You must correctly specify the location of \n the file, its format or the correct \n link of the YT video.", font=font)
    error_description_3.grid(row=0, column=0, padx=10, pady=20)

    # Confirmation button
    confirmation_button_3 = ctk.CTkButton(
        master=pop_up_3, width=50, text="OK", corner_radius=5, command=lambda: quit_pop_up(pop_up=pop_up_3), fg_color="#541690", hover_color="#2c0e47")
    confirmation_button_3.grid(row=1, column=0, pady=50, padx=125)


def quit_pop_up(pop_up):
    pop_up.destroy()
    pop_up.update()


def download_video():

    try:
        Choice = remember_choice()
        Yt = YouTube(link_entry.get())

        # Mp4 choice
        if Choice == 1:
            mp4 = Yt.streams.get_highest_resolution()
            DownloadedVideo1 = mp4.download(output_path=location_list[0])
            success()

        # Mp3 choice
        elif Choice == 2:
            mp3 = Yt.streams.get_audio_only()
            DownloadedVideo2 = mp3.download(output_path=location_list[0])
            base, ext = os.path.splitext(DownloadedVideo2)
            NewFile = base + ".mp3"
            os.rename(DownloadedVideo2, NewFile)
            success()

    # Error
    except:
        error()

    location_list.clear()


def remember_choice():
    return selected_format.get()

# UI Setup


ctk.set_appearance_mode("System")
App = ctk.CTk()
App.geometry("700x650")
App.title("YT Downloader by Marek Baranski")

# Variables

font = ("Noto Sans", 13)

selected_format = ctk.IntVar()

location_list = []

# Appearance mode

appearance_mode_label = ctk.CTkLabel(
    master=App, text="Appearance mode: ", text_color="#541690", font=font)
appearance_mode_label.grid(row=0, column=0, pady=10)

appearance_mode_optionmenu = ctk.CTkOptionMenu(master=App, values=[
    "System", "Dark", "Light"], fg_color="#541690", button_color="#541690", button_hover_color="#2c0e47", dropdown_hover_color="#2c0e47", command=change_appearance_mode_event)
appearance_mode_optionmenu.grid(row=1, column=0, padx=30)

# Scaling mode

scaling_label = ctk.CTkLabel(
    master=App, text="UI Scaling: ", text_color="#541690", font=font)

scaling_label.grid(row=0, column=2, pady=10)

scaling_optionmenu = ctk.CTkOptionMenu(master=App, values=[
    "80%", "90%", "100%", "110%", "120%"], fg_color="#541690",  button_color="#541690", button_hover_color="#2c0e47",  dropdown_hover_color="#2c0e47", command=change_scaling_event)
scaling_optionmenu.set("100%")
scaling_optionmenu.grid(row=1, column=2, padx=30)

# Logo
logo = ctk.CTkImage(Image.open("3721679-youtube_108064.ico"), size=(200, 200))

logo_display = ctk.CTkLabel(master=App, image=logo, text="", padx=20, pady=20)
logo_display.grid(row=2, column=1, padx=1, pady=50)

App.iconbitmap("3721679-youtube_108064.ico")

# Location
choose_location = ctk.CTkButton(master=App, width=300, text="Choose a file location",
                                corner_radius=5, fg_color="#FF4949", hover_color="#CC3F3F", command=select_folder, text_color="black")
choose_location.grid(row=3, column=1, pady=10)

# Location Label
file_path_description = ctk.CTkLabel(
    master=App, text="File location: N/A", text_color="#FF4949", font=font)
file_path_description.grid(row=4, column=1, padx=10, pady=0)


# Link
link_entry = ctk.CTkEntry(master=App, placeholder_text="Input YT video link",
                          width=300, fg_color="#FF8D29", placeholder_text_color="black", text_color="black", border_color="#FF8D29", corner_radius=5)
link_entry.grid(row=5, column=1, pady=10)

#Mp4 / Mp3

mp4_button = ctk.CTkRadioButton(
    master=App, text="Mp4", text_color="#FFCD38", hover_color="#FFCD38", fg_color="#FFCD38", variable=selected_format, command=remember_choice, value=1)
mp4_button.grid(row=6, column=1, columnspan=1, pady=10)

mp3_button = ctk.CTkRadioButton(
    master=App, text="Mp3", text_color="#FFCD38", hover_color="#FFCD38", fg_color="#FFCD38", variable=selected_format, command=remember_choice, value=2)
mp3_button.grid(row=6, column=1, columnspan=2, pady=10)

# Download
download_vid = ctk.CTkButton(master=App, width=300, text="Download video", corner_radius=5,
                             fg_color="#FFCD38", hover_color="#E6B924", text_color="black", command=download_video)
download_vid.grid(row=7, column=1, pady=10)

App.mainloop()
