# **Technical Architecture**

## **1. File Structure**
- **`main.py`:** Implements the UI and core application logic.
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

## **1. Clone the Repository**
```bash
git clone https://github.com/YourUsername/JPass_Password_Manager.git
cd JPass_Password_Manager

![authenticate](https://github.com/user-attachments/assets/c7be4e1d-d2fa-4c3e-946b-de93f54d3fe0)
