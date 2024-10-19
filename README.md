Öncelikle bu dosyaların proje dersleri için izinsiz (ç)alınması ve kullanılması yasaktır.Lütfen kendi dersinizi geçmek için kendi çabanızı kullanın. Lütfen benden izin alıp kullanınız.

Mühendislik Tasarımı dersim için yapmış oldupumm IoT temelli robot kol projesidir.

Raspberry Pi 4 ve MG995 servo kullanılarak yapılmış bir 3 eklem robot kol projesidir.

Proje temel olarak Python'un tkinter kütüphanesi ile yazılmış arayüzden sizden hangi servonun kaç derece döndürülmesinin gerektiğini öğrenir ve Raspberry Pi 4'ün gerekli GPIO pinlerine bağlı servoları buna göre döndürür. İşlem tamamlandıktan sonra geribildirim olarak matplotlib kütüphanesi sayesinde tasarladığımız kartezyen koordinat sistemden robot kolun o anki konumunu görselleştirir. Raspberry Pi 4'e RealVNCViewer ile bağlanıp arayüzü Raspberry üzerinden çalıştırdığımız için tamamen kablosuz şekilde çalışmaktadır. İhtiyaca göre databse ile kolayca bir şekilde bağlantı kurulup tamamen uzaktann kontrol edilebilecek şekilde revize edilebilir.

*----------------------------------------------------------------------------------------------------------------*

If u use it please ask a premission first.Otherwise it would be stealing.

Here's my Robotic Arm project for my Engineering Design class.

This is a 3 DOF Robotic Arm project with using Raspberry Pi 4 amd MG995 Servo motors.

Basically , robotic arm get degrees and axis from GUI (written by using tkinter library for python) and Raspberry Pi 4 sending PWM signals to the servos.After movement completed GUI visualize robotic arm's location with using by matplotlib library of python.I connected Raspberry using by RealVNCViewer . If you want to make it remote control you can do it by just adding databes connection easily
