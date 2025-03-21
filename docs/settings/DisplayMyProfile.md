# Display My Profile

**Technical Name:** DisplayMyProfile

**Category:** User Management

**Default Value:** Not explicitly mentioned

**Impact Level:** Medium

**Description:**

The `DisplayMyProfile` parameter controls whether the user's profile and related information are displayed within the Pathlock Cloud GRC platform. This includes handling of user images and profile details visibility across the platform.

**Business Impact:**

Enabling this feature enhances user experience by allowing users to see their own profile information, which can improve interaction with the GRC platform. It supports user engagement by making the interface more personal and user-friendly.

**Technical Impact when configured:**

When enabled, the system will display the user's profile picture and relevant information across different sections of the platform. If the modern style setting is active, it attempts to load an external image link for the user's profile picture. Otherwise, it defaults to a generic user icon. This feature's proper functioning depends on the `EnableModernStyle` setting in `CommonSettings`.

**Examples Scenario:**

- A company wants to ensure that their users have a more personalized experience on the GRC platform. By enabling the `DisplayMyProfile` feature, each user's profile picture and name are displayed, making the interface feel more tailored to the individual.

**Related Settings:**

- `EnableModernStyle` in `CommonSettings`: Determines whether a modern styling is applied, including how profile pictures are handled.

**Best Practices:** configure when the organization wants to enhance user interaction with the platform by making it more personalized. Avoid when minimalistic UI is preferred or in environments with strict privacy concerns regarding user photos and profile details.