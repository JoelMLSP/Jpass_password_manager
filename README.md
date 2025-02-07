# **Technical Architecture**

## **1. File Structure**
- **`main.py`:** Implements the UI and core application logic.
- **`Jpass Authentication.py`:** Handles user creation and authentication.
- **`passgen.py`:** Handles password generation.
- **`data.json`:** Stores passwords.
- **`user.json`:** Contains user credentials.

---

## **2. Key Functions**

### **Authentication**
- **Login Handling:**
  - Matches credentials entered by the user with those stored in `user.json`.
- **Registration:**
  - Allows users to create a new account if no credentials are stored.

### **Password Management**
- **Save Passwords:**
  - Adds or updates credentials in `data.json` with website name, username, and password fields.
- **Search Passwords:**
  - Retrieves credentials by matching website names from `data.json`.

### **Password Generation**
- Utilizes a customizable algorithm to create strong, random passwords.

---

## **3. Limitations and Future Improvements**
- **Current Storage Method:**
  - Passwords and credentials are stored in JSON files, which are not encrypted by default. Integrating encryption (e.g., AES) would significantly enhance confidentiality.
- **Multi-User Support:**
  - The current implementation supports only one user at a time. Future updates could introduce multiple user profiles.

---

# **Setup Guide**



![authenticate](https://github.com/user-attachments/assets/c7be4e1d-d2fa-4c3e-946b-de93f54d3fe0)

you can use the register button to register your user, if no database exists one will be created

![image](https://github.com/user-attachments/assets/fabcb8cd-43ec-440f-9826-f2ad860cb800)

you can then login and will have a authentication message if password matches with the one stored in the database

![image](https://github.com/user-attachments/assets/8109628e-d60a-4438-bf64-6b8538964ab2)

once signed in you can add passwords, username, and sites. Sites can be fetched by filling in the part of the website ie (Ama for Amazon) 

![image](https://github.com/user-attachments/assets/41ad0130-a16d-46bc-be14-f5cd2401052c)


if no other matches are close it will fetch the details and automatically copy the password for easy pasting in your browser.

![image](https://github.com/user-attachments/assets/8927b329-ec83-4a75-949d-bd58f83f5207)


## **1. Clone the Repository**
```bash
git clone https://github.com/YourUsername/JPass_Password_Manager.git
cd JPass_Password_Manager


