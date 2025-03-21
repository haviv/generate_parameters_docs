**Technical Name: CodePage**

**Category: Configuration**

**Default Value:**

**Impact Level: Medium**

**Description:**

The CodePage parameter affects the encoding used in the export process of various report formats. It plays a crucial role in determining how text is rendered and ensures compatibility across different systems and locales.

**Business Impact:**

Correctly setting the CodePage parameter ensures that exported reports (such as CSV, XLS, HTML formats) are accurately rendered and readable, regardless of the regional settings or the default character encoding of the end user's system. It prevents data corruption and garbled text in reports, facilitating seamless data interpretation and decision-making.

**Technical Impact when configured:**

Proper configuration of the CodePage parameter ensures that exported files maintain textual integrity when opened in different software or systems. It prevents character mismatches and ensures that special characters and non-English characters are displayed correctly.

**Examples Scenario:**

A multinational corporation needs to generate compliance reports in CSV format that include data in European languages with special characters. By setting the CodePage parameter correctly, they ensure that these characters are accurately represented in the exported file, preventing misunderstandings or data corruption when these reports are shared across regional offices.

**Related Settings:**

- Charset settings in HTTP Responses
- ExportFormats (e.g., XLS, XLSX, CSV, HTML)

**Best Practices:** configure when dealing with internationalization or when special characters need to be preserved across different system locales. Avoid generic configurations when the target audience or systems are known and have specific encoding requirements.