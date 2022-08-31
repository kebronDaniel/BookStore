# Generated by Django 4.1 on 2022-08-31 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0005_alter_order_placed_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "payment_options",
                    models.CharField(
                        choices=[
                            ("c", "credit card"),
                            ("d", "debit card"),
                            ("p", "paypal"),
                        ],
                        default="c",
                        max_length=1,
                    ),
                ),
                ("name_on_the_card", models.CharField(max_length=250)),
                ("credit_card_number", models.PositiveIntegerField()),
                ("expiration", models.DateTimeField(null=True)),
                ("cvv", models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name="book",
            name="image",
            field=models.URLField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="payment",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="books.payment",
            ),
        ),
    ]
