from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from doctors.models import Doctor
from services.models import Service, Record, Diagnostic
from users.models import User


class TestService(TestCase):
    """ Тестирование сервиса """

    def setUp(self):
        self.service = Service.objects.create(name="TEST1",
                                              description="Электрокардиография",
                                              price=7000.00)
        self.user = User.objects.create(email='admin@example.com')
        self.doctor = Doctor.objects.create(name="Филатов",
                                            surname="Андрей",
                                            patronymic="Владимирович",
                                            work_experience=15,
                                            specialization="Кардиолог",
                                            science="врач высшей категории",
                                            post="Кардиолог", )
        self.record = Record.objects.create(user=self.user,
                                            service=self.service,
                                            doctor=self.doctor,
                                            record_time="2025-01-09")
        self.client = Client()
        self.list_url = reverse('services:home')
        self.create_url = reverse('services:create')
        self.detail_url = reverse('services:service_detail', args=[self.service.pk])

    def test_create_service(self):
        """ Тестирование создания сервиса """

        response = self.client.post(self.create_url, {"name": "TEST2",
                                                      "description": "Электрокардиография",
                                                      "price": '8000.00', })

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(Service.objects.all().count(), 1)
        self.assertEqual(self.service.name, "TEST1")

    def test_list_service(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'services/home.html')

    def test_detail_service(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_delete_service(self):
        """ Тестирование удаления сервиса """

        url = reverse("services:delete", args=(self.service.pk,))
        data = {
            "name": "TEST1",
            "description": "Электрокардиография",
            "price": '7000.00',
        }

        response = self.client.delete(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_edit_service(self):
        """ Тестирование изменения сервиса """

        url = reverse("services:edit", args=(self.service.pk,))
        data = {
            "name": "TEST2",
            "description": "Электрокардиография",
            "price": '8000.00',
        }

        response = self.client.put(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(data.get("name"), "TEST2")
        self.assertEqual(data.get("description"), "Электрокардиография")
        self.assertEqual(data.get("price"), '8000.00')


class TestRecord(TestCase):
    """ Тестирование записи """

    def setUp(self):
        self.service = Service.objects.create(name="TEST1",
                                              description="Электрокардиография",
                                              price=8000.00)
        self.user = User.objects.create(email='testuser@example.com')
        self.doctor = Doctor.objects.create(name="Филатов",
                                            surname="Андрей",
                                            patronymic="Владимирович",
                                            work_experience=15,
                                            specialization="Кардиолог",
                                            science="врач высшей категории",
                                            post="Кардиолог", )
        self.record = Record.objects.create(user=self.user,
                                            service=self.service,
                                            doctor=self.doctor,
                                            record_time="2025-01-09")
        self.client = Client()
        self.list_url = reverse('services:record_list')
        self.create_url = reverse('services:record')

    def test_create_record(self):
        """ Тестирование создания записи """

        data = {
            "user": self.user,
            "service": self.service,
            "doctor": self.doctor,
            "record_time": "2025-01-09"
        }
        response = self.client.post(self.create_url, data=data)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(Record.objects.all().count(), 1)
        self.assertEqual(self.record.user.email, 'admin@example.com')
        self.assertEqual(self.record.service.name, "TEST1")
        self.assertEqual(self.record.doctor.specialization, "врач высшей категории")

    def test_list_record(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'services/record_list.html')

    def test_delete_record(self):
        """ Тестирование удаления записи """

        url = reverse("services:record_delete", args=(self.record.pk,))
        data = {
            "user": self.user,
            "service": self.service,
            "doctor": self.doctor,
            "record_time": "2025-01-09"
        }

        response = self.client.delete(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_edit_record(self):
        """ Тестирование изменения записи """

        url = reverse("services:record_edit", args=(self.record.pk,))
        doctor = Doctor.objects.create(name="Елисеев",
                                       surname="Александр",
                                       patronymic="Викторович",
                                       work_experience=10,
                                       specialization="Уролог / гинеколог",
                                       science="врач высшей категории",
                                       post="Уролог / гинеколог", )

        data = {
            "user": self.user,
            "service": self.service,
            "doctor": doctor,
            "record_time": "2025-01-09"
        }

        response = self.client.put(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(Record.objects.all().count(), 1)
        self.assertEqual(self.record.user.email, 'admin@example.com')
        self.assertEqual(self.record.service.name, "TEST1")
        self.assertEqual(self.record.doctor.specialization, "врач высшей категории")


class TestDiagnostic(TestCase):
    """ Тестирование результата """

    def setUp(self):
        self.service = Service.objects.create(name="TEST1",
                                              description="Электрокардиография",
                                              price=7000.00)
        self.user = User.objects.create(email='admin@example.com')
        self.doctor = Doctor.objects.create(name="Филатов",
                                            surname="Андрей",
                                            patronymic="Владимирович",
                                            work_experience=15,
                                            specialization="Кардиолог",
                                            science="врач высшей категории",
                                            post="Кардиолог", )
        self.record = Record.objects.create(user=self.user,
                                            service=self.service,
                                            doctor=self.doctor,
                                            record_time="2025-01-09")
        self.diagnostic = Diagnostic.objects.create(user=self.user,
                                                    record=self.record,
                                                    result="Test",
                                                    diagnose="Test_diagnose"
                                                    )
        self.client = Client()
        self.list_url = reverse('services:diagnostic_list')

    def test_list_diagnostic(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(self.diagnostic.user.email, 'admin@example.com')
        self.assertEqual(self.diagnostic.record.pk, 1)
        self.assertEqual(self.diagnostic.diagnose, "Test_diagnose")