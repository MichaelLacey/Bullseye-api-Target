from app.models import db, Product_Images, environment, SCHEMA


def seed_product_images():

    # Electronic product images
    product1_img1 = Product_Image(product_id=1, image_url='https://target.scene7.com/is/image/Target/GUEST_9245620b-5c8a-49a2-a9b7-8ea9d2c6705a?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product1_img2 = Product_Image(product_id=1, image_url='https://target.scene7.com/is/image/Target/GUEST_7e0f014a-c8b0-4267-bd2d-97e4e96c00d4?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product1_img3 = Product_Image(product_id=1, image_url='https://target.scene7.com/is/image/Target/GUEST_fbaf08e3-a7fe-4ac5-a1ca-ed3fbff22b89?wid=1000&hei=1000&qlt=80&fmt=webp')
    product1_img4 = Product_Image(product_id=1, image_url='https://target.scene7.com/is/image/Target/GUEST_a96425ae-6110-4ff2-b91e-583aeafc83fd?wid=1000&hei=1000&qlt=80&fmt=webp')

    product2_img1 = Product_Image(product_id=2, image_url='https://target.scene7.com/is/image/Target/GUEST_75612b8a-4ad0-4644-a8c5-ac9305db59a5?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product2_img2 = Product_Image(product_id=2, image_url='https://target.scene7.com/is/image/Target/GUEST_ba4e5e43-6995-4ff2-a16b-884330861839?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product2_img3 = Product_Image(product_id=2, image_url='https://target.scene7.com/is/image/Target/GUEST_f62ae9f8-08df-4657-8281-dca86674ce23?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product2_img4 = Product_Image(product_id=2, image_url='https://target.scene7.com/is/image/Target/GUEST_4bcaf7b4-0291-4a82-881e-fe8518ad3f0f?wid=1000&hei=1000&qlt=80&fmt=webp')

    product3_img1 = Product_Image(product_id=3, image_url='https://target.scene7.com/is/image/Target/GUEST_710e3484-be95-4ff0-ad24-f5b43228900d?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product3_img2 = Product_Image(product_id=3, image_url='https://target.scene7.com/is/image/Target/GUEST_1ca220c9-fd95-4496-8f20-c4e07f9ce6d5?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product3_img3 = Product_Image(product_id=3, image_url='https://target.scene7.com/is/image/Target/GUEST_7de012d4-4cf5-497a-af4b-993299bc22c5?wid=1000&hei=1000&qlt=80&fmt=webp')
    product3_img4 = Product_Image(product_id=3, image_url='https://target.scene7.com/is/image/Target/GUEST_ede62405-c7e8-481d-aaa6-2631a0267d20?wid=1000&hei=1000&qlt=80&fmt=webp')

    product4_img1 = Product_Image(product_id=4, image_url='https://target.scene7.com/is/image/Target/GUEST_c3afdca6-eb60-4533-a7f5-741451cfd6cd?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product4_img2 = Product_Image(product_id=4, image_url='https://target.scene7.com/is/image/Target/GUEST_1bf09891-44f5-4992-a411-5c67721b759f?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product4_img3 = Product_Image(product_id=4, image_url='https://target.scene7.com/is/image/Target/GUEST_782c6793-2760-43a1-b9e1-5feb95106363?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product4_img4 = Product_Image(product_id=4, image_url='https://target.scene7.com/is/image/Target/GUEST_bbdedb5b-0cb8-4b43-bea0-9bb25064ff31?wid=1000&hei=1000&qlt=80&fmt=webp')

    product5_img1 = Product_Image(product_id=5, image_url='https://target.scene7.com/is/image/Target/GUEST_5b7417ae-41e4-495d-8c9c-8af0c4ccf993?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product5_img2 = Product_Image(product_id=5, image_url='https://target.scene7.com/is/image/Target/GUEST_550eb80b-1ac2-4855-a5e5-11e7f334be41')
    product5_img3 = Product_Image(product_id=5, image_url='https://target.scene7.com/is/image/Target/GUEST_22a33d9b-1232-4e5b-b0a6-487b99d9ec59?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product5_img4 = Product_Image(product_id=5, image_url='https://target.scene7.com/is/image/Target/GUEST_28f6c447-b3bd-4403-b729-1ca20c485b77?wid=1000&hei=1000&qlt=80&fmt=webp')

    product6_img1 = Product_Image(product_id=6, image_url='https://target.scene7.com/is/image/Target/GUEST_49f3614e-c392-440f-ab24-7dd7ad5df504?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product6_img2 = Product_Image(product_id=6, image_url='https://target.scene7.com/is/image/Target/GUEST_505ec2c3-bdca-4590-846f-356009959f3d?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product6_img3 = Product_Image(product_id=6, image_url='https://target.scene7.com/is/image/Target/GUEST_29f464d7-7f87-4306-b358-8b0809c162bd?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product6_img4 = Product_Image(product_id=6, image_url='https://target.scene7.com/is/image/Target/GUEST_d9abec29-1ef3-456a-a268-3036ab66d9ce?wid=1000&hei=1000&qlt=80&fmt=webp')

    product7_img1 = Product_Image(product_id=7, image_url='https://target.scene7.com/is/image/Target/GUEST_3bb8b683-f0a7-4b7e-8207-ea716a72f41d?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product7_img2 = Product_Image(product_id=7, image_url='https://target.scene7.com/is/image/Target/GUEST_23069a99-5978-40fd-a236-acd2809eb615?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product7_img3 = Product_Image(product_id=7, image_url='https://target.scene7.com/is/image/Target/GUEST_e2f6801d-984b-4239-b7ce-d85a23f22478?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product7_img4 = Product_Image(product_id=7, image_url='https://target.scene7.com/is/image/Target/GUEST_3a20a452-84f2-4449-abc4-5e2fcd0b94d6?wid=325&hei=325&qlt=80&fmt=pjpeg')

    product8_img1 = Product_Image(product_id=8, image_url='https://target.scene7.com/is/image/Target/GUEST_d481ae28-76cf-45fc-a28b-0dca314d449c?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product8_img2 = Product_Image(product_id=8, image_url='https://target.scene7.com/is/image/Target/GUEST_6b120943-a30a-4f67-86ad-c68e8f6a6263?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product8_img3 = Product_Image(product_id=8, image_url='https://target.scene7.com/is/image/Target/GUEST_dfd1cf3d-6a14-47cb-8de7-eac25ffa938c?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product8_img4 = Product_Image(product_id=8, image_url='https://target.scene7.com/is/image/Target/GUEST_15cd26e7-ef1e-4932-9e94-570420e5529e?wid=1000&hei=1000&qlt=80&fmt=webp')

    product9_img1 = Product_Image(product_id=9, image_url='https://target.scene7.com/is/image/Target/GUEST_4020069d-7653-4fab-a6f2-df3d1686ef21?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product9_img2 = Product_Image(product_id=9, image_url='https://target.scene7.com/is/image/Target/GUEST_2a142611-c80c-4729-8680-89f9b0e6376d?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product9_img3 = Product_Image(product_id=9, image_url='https://target.scene7.com/is/image/Target/GUEST_b7aa418e-30da-4001-81dc-122c13b62673?wid=1000&hei=1000&qlt=80&fmt=webp')
    product9_img4 = Product_Image(product_id=9, image_url='https://edge.curalate.com/v1/img/RwS96Vcwb3GYa1LwjcM4MYdgg02nVWnR4TCwyUEp0sQ=/h/700?compression=0.85&fit=constrain')

    product10_img1 = Product_Image(product_id=10, image_url='https://target.scene7.com/is/image/Target/GUEST_4e1df04a-6e27-4837-8503-53e0277c12af?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product10_img2 = Product_Image(product_id=10, image_url='https://target.scene7.com/is/image/Target/GUEST_940dd689-40fe-428d-9d7c-2f7dcdc1d600?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product10_img3 = Product_Image(product_id=10, image_url='https://target.scene7.com/is/image/Target/GUEST_c81c5fb6-ba2d-4ebc-9e1d-e19718138cdc?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product10_img4 = Product_Image(product_id=10, image_url='https://target.scene7.com/is/image/Target/GUEST_9228309a-693b-4011-a5b3-29a8dcf85cf4?wid=1000&hei=1000&qlt=80&fmt=webp')

    product11_img1 = Product_Image(product_id=11, image_url='https://target.scene7.com/is/image/Target/GUEST_b336a8fb-2f44-46a1-840a-6d51f2226f53?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product11_img2 = Product_Image(product_id=11, image_url='https://target.scene7.com/is/image/Target/GUEST_051a0c12-4cfc-4f7d-827b-6e475313ce8a?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product11_img3 = Product_Image(product_id=11, image_url='https://target.scene7.com/is/image/Target/GUEST_a0ab301d-26bc-47b1-abf5-aaef060bf2b6?wid=1000&hei=1000&qlt=80&fmt=webp')
    product11_img4 = Product_Image(product_id=11, image_url='https://target.scene7.com/is/image/Target/GUEST_6b37bd61-c5d6-4531-8915-22e359ea33af?qlt=85&fmt=webp&hei=700&fit=constrain')

    product12_img1 = Product_Image(product_id=12, image_url='https://target.scene7.com/is/image/Target/GUEST_410b4fa2-a8db-48be-90f7-df47577f3be5?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product12_img2 = Product_Image(product_id=12, image_url='https://target.scene7.com/is/image/Target/GUEST_88344900-c1c2-4a22-a954-416396e588b8?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product12_img3 = Product_Image(product_id=12, image_url='https://target.scene7.com/is/image/Target/GUEST_867f75c2-d714-493a-a5a0-3e1b69d019cc?wid=1000&hei=1000&qlt=80&fmt=webp')
    product12_img4 = Product_Image(product_id=12, image_url='https://target.scene7.com/is/image/Target/GUEST_2b0b80f7-6fd4-495a-b5ee-a03116dffdbb?wid=325&hei=325&qlt=80&fmt=pjpeg')


    db.session.add(product1_img1)
    db.session.add(product1_img2)
    db.session.add(product1_img3)
    db.session.add(product1_img4)

    db.session.add(product2_img1)
    db.session.add(product2_img2)
    db.session.add(product2_img3)
    db.session.add(product2_img4)

    db.session.add(product3_img1)
    db.session.add(product3_img2)
    db.session.add(product3_img3)
    db.session.add(product3_img4)

    db.session.add(product4_img1)
    db.session.add(product4_img2)
    db.session.add(product4_img3)
    db.session.add(product4_img4)

    db.session.add(product5_img1)
    db.session.add(product5_img2)
    db.session.add(product5_img3)
    db.session.add(product5_img4)

    db.session.add(product6_img1)
    db.session.add(product6_img2)
    db.session.add(product6_img3)
    db.session.add(product6_img4)

    db.session.add(product7_img1)
    db.session.add(product7_img2)
    db.session.add(product7_img3)
    db.session.add(product7_img4)

    db.session.add(product9_img1)
    db.session.add(product9_img2)
    db.session.add(product9_img3)
    db.session.add(product9_img4)

    db.session.add(product10_img1)
    db.session.add(product10_img2)
    db.session.add(product10_img3)
    db.session.add(product10_img4)

    db.session.add(product11_img1)
    db.session.add(product11_img2)
    db.session.add(product11_img3)
    db.session.add(product11_img4)

    db.session.add(product12_img1)
    db.session.add(product12_img2)
    db.session.add(product12_img3)
    db.session.add(product12_img4)


    db.session.add()
    db.session.add()
    db.session.commit()


    def undo_product_images():
        if environment == "production":
            db.session.execute(f"TRUNCATE table {SCHEMA}.product_images RESTART IDENTITY CASCADE;")
        else:
            db.session.execute("DELETE FROM product_images")
            
            db.session.commit()