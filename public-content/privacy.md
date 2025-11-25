## Política de Privacidad: Declaración de Principios

En **Overseer**, la protección de datos no es una opción comercial, sino una **obligación moral y legal**.  
Este documento establece de forma clara y vinculante el alcance, límites y fundamentos de nuestro tratamiento de datos.

---

### 1. Privacidad incorporada desde el diseño
Overseer ha sido desarrollado bajo el principio de **“Privacy by Design”**.  
Su arquitectura técnica minimiza de forma estructural la exposición de información personal:

- **No recopilación:** La plataforma no solicita ni procesa datos personales identificables.  
- **No autenticación tradicional:** No requerimos correos electrónicos, contraseñas ni números telefónicos.  
- **Cifrado de extremo a extremo:** Utilizamos el estándar AES-256, con claves que permanecen exclusivamente en el dispositivo del usuario.  
- **Autenticación anónima:** El sistema opera mediante Passkeys que no asocian la identidad del usuario con su actividad dentro de la plataforma.

---

### 2. Información que no recolectamos
Overseer excluye deliberadamente la recolección de la siguiente información:

- Nombres, direcciones de correo o contraseñas  
- Direcciones IP, geolocalización o huellas digitales del navegador  
- Cookies de seguimiento o analítica de terceros  
- Integraciones con redes sociales o servicios externos

---

### 3. Datos tratados y medidas de protección
Overseer únicamente trata **datos funcionales necesarios** para operar, bajo un modelo de aislamiento de instancia y cifrado persistente:

- **Datos funcionales:** Asignaciones, territorios y demás entradas se cifran en origen y se almacenan bajo control exclusivo del usuario.  
- **Instancias aisladas:** Cada base de datos es independiente, anónima y cifrada con claves individuales.  
- **Seguridad en tránsito:** Toda comunicación se realiza sobre TLS 1.3 con **Perfect Forward Secrecy** habilitado.

---

### 4. Control exclusivo del usuario
La clave de acceso (**Passkey**) es intransferible y **no está almacenada por Overseer**.  
El acceso a los datos es exclusivo del usuario.  
En caso de pérdida de la Passkey, la información es **irrecuperable**.

---

### 5. Prohibición absoluta de cesión de datos
Overseer **no comparte, transfiere ni vende datos** a ninguna entidad, incluidas:

- Autoridades gubernamentales  
- Entidades regulatorias  
- Empresas con fines de lucro  
- Plataformas de marketing o publicidad  
- Proveedores de servicios externos, incluso bajo solicitud formal

---

### 6. Eliminación definitiva de la información
El usuario puede solicitar la eliminación de su instancia en cualquier momento.  
Asimismo, se procederá a la eliminación automática tras un periodo prolongado de inactividad.  
Dicha eliminación comprende:

- Borrado seguro de los archivos cifrados  
- Eliminación permanente de copias de respaldo  
- Revocación irreversible de la clave de acceso

---

### 7. Cumplimiento legal internacional
Overseer opera conforme a la **Ley Federal de Protección de Datos suiza (LPD)** y se adhiere a principios internacionales como el **Reglamento General de Protección de Datos (GDPR)**, cuando aplique.  
No reconocemos jurisdicciones que comprometan el estándar de privacidad establecido.

---

### 8. Transparencia operativa
El código fuente de Overseer está disponible públicamente.  
Está sujeto a auditorías independientes bajo licencias de software libre.  
No implementamos telemetría ni recopilación encubierta de datos.

---

### 9. Ejercicio de derechos ARCO
Los usuarios pueden ejercer sus derechos de **acceso, rectificación, cancelación u oposición (ARCO)** de forma completamente anónima a través del sistema integrado **Overseer A/I Support**.  
No se ofrece atención por correo electrónico, redes sociales ni canales externos.

---

### 10. Vigencia y modificaciones
Esta política puede ser modificada para garantizar su actualización normativa y técnica.  
No obstante, ningún cambio reducirá el nivel de protección de datos previamente otorgado.  
Las modificaciones serán notificadas a través de esta página.

---

**Overseer no es un producto. Es una convicción: la privacidad no se negocia.**
