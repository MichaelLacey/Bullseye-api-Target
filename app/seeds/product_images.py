from app.models import db, Product_Image, environment, SCHEMA


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

    db.session.add(product8_img1)
    db.session.add(product8_img2)
    db.session.add(product8_img3)
    db.session.add(product8_img4)

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

    #  Household essentials(2) product images
    product13_img1 = Product_Image(product_id=13, image_url='https://target.scene7.com/is/image/Target/GUEST_265faf09-7b5e-4735-9eec-cba0f7c581a1?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product13_img2 = Product_Image(product_id=13, image_url='https://target.scene7.com/is/image/Target/GUEST_f74f5f70-7267-443e-9af9-f2a7f0af2907?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product13_img3 = Product_Image(product_id=13, image_url='https://target.scene7.com/is/image/Target/GUEST_2d39a25c-a674-4a73-9df1-3801f01fbe59?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product13_img4 = Product_Image(product_id=13, image_url='https://target.scene7.com/is/image/Target/GUEST_3372d6df-baf5-438a-a90f-6a564fa978af?wid=1000&hei=1000&qlt=80&fmt=webp')

    product14_img1 = Product_Image(product_id=14, image_url='https://target.scene7.com/is/image/Target/GUEST_69983684-0464-430d-acb6-f228a0845dfb?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product14_img2 = Product_Image(product_id=14, image_url='https://target.scene7.com/is/image/Target/GUEST_64089630-e7d4-4636-af15-27c9c204acbc?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product14_img3 = Product_Image(product_id=14, image_url='https://target.scene7.com/is/image/Target/GUEST_fffd5848-37c7-48b4-b4c6-8f11bb495be6?wid=1000&hei=1000&qlt=80&fmt=webp')
    product14_img4 = Product_Image(product_id=14, image_url='https://target.scene7.com/is/image/Target/GUEST_8ff8db58-aea5-4321-a7ce-23605b44fed7?wid=1000&hei=1000&qlt=80&fmt=webp')

    product15_img1 = Product_Image(product_id=15, image_url='https://target.scene7.com/is/image/Target/GUEST_cbec208a-7db1-462c-bf48-666a9c6a0b35?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product15_img2 = Product_Image(product_id=15, image_url='https://target.scene7.com/is/image/Target/GUEST_f833659b-e651-4449-b404-5274a332abd9?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product15_img3 = Product_Image(product_id=15, image_url='https://target.scene7.com/is/image/Target/GUEST_2289a499-cdd2-46f0-8cae-1fe890bcb492?wid=1000&hei=1000&qlt=80&fmt=webp')
    product15_img4 = Product_Image(product_id=15, image_url='https://target.scene7.com/is/image/Target/GUEST_4f2bbaa5-4b09-4851-a6db-e06b84c40dad?wid=1000&hei=1000&qlt=80&fmt=webp')

    product16_img1 = Product_Image(product_id=16, image_url='https://target.scene7.com/is/image/Target/GUEST_e9f4d15a-846d-449b-bb3f-3040b9fb88f0?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product16_img2 = Product_Image(product_id=16, image_url='https://target.scene7.com/is/image/Target/GUEST_3be8c2b5-383a-479b-b178-40559142db5c?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product16_img3 = Product_Image(product_id=16, image_url='https://target.scene7.com/is/image/Target/GUEST_37ecc2b6-29a4-45d1-a3f0-ad1d1dd591be?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product16_img4 = Product_Image(product_id=16, image_url='https://target.scene7.com/is/image/Target/GUEST_2c5b7595-6260-4529-8c1f-46272fd040e1?wid=1000&hei=1000&qlt=80&fmt=webp')

    product17_img1 = Product_Image(product_id=17, image_url='https://target.scene7.com/is/image/Target/GUEST_a1bc23c0-ccde-4a2b-99da-1b7e1907abed?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product17_img2 = Product_Image(product_id=17, image_url='https://target.scene7.com/is/image/Target/GUEST_42b88ab5-e05d-4f78-a304-f03039ef89c3?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product17_img3 = Product_Image(product_id=17, image_url='https://edge.curalate.com/v1/img/k7IzjwiOlgjjDVuwUdK-_XQ691rg_T8Elu6UZPfTmmU=/h/700?compression=0.85&fit=constrain')
    product17_img4 = Product_Image(product_id=17, image_url='https://target.scene7.com/is/image/Target/GUEST_ebbe66b1-c1e8-420c-ace8-da0b921294b4?wid=1000&hei=1000&qlt=80&fmt=webp')

    product18_img1 = Product_Image(product_id=18, image_url='https://target.scene7.com/is/image/Target/GUEST_fc37916c-e5b3-4550-9686-4cc4ff0370b7?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product18_img2 = Product_Image(product_id=18, image_url='https://target.scene7.com/is/image/Target/GUEST_0b151f5b-b05f-4892-9627-65d4bd9f87b7?wid=1000&hei=1000&qlt=80&fmt=webp')
    product18_img3 = Product_Image(product_id=18, image_url='https://target.scene7.com/is/image/Target/GUEST_0ba29e26-1158-419f-bd38-5f45c1978d4e?wid=1000&hei=1000&qlt=80&fmt=webp')
    product18_img4 = Product_Image(product_id=18, image_url='https://edge.curalate.com/v1/img/hQxJFNpAf-ZYiSnmg3RJHJmghodtXl8fL8RehR-rxUY=/h/700?compression=0.85&fit=constrain')

    product19_img1 = Product_Image(product_id=19, image_url='https://target.scene7.com/is/image/Target/GUEST_e8d2f4ac-49bd-450a-9305-1042669509c8?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product19_img2 = Product_Image(product_id=19, image_url='https://target.scene7.com/is/image/Target/GUEST_fd248897-4645-4b82-b59a-8176f42db218?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product19_img3 = Product_Image(product_id=19, image_url='https://target.scene7.com/is/image/Target/GUEST_74debb3c-282f-4242-ae9f-2bed892281c7?wid=1000&hei=1000&qlt=80&fmt=webp')
    product19_img4 = Product_Image(product_id=19, image_url='https://target.scene7.com/is/image/Target/GUEST_74a034c5-a79e-4ad6-ac1e-ed956e8a4a72?wid=1000&hei=1000&qlt=80&fmt=webp')

    product20_img1 = Product_Image(product_id=20, image_url='https://target.scene7.com/is/image/Target/GUEST_ee613317-8f45-417d-9c8a-dc81bb3198b9?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product20_img2 = Product_Image(product_id=20, image_url='https://target.scene7.com/is/image/Target/GUEST_e5c8bcf3-f91a-4121-b4c3-bd9d18f87a20?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product20_img3 = Product_Image(product_id=20, image_url='https://target.scene7.com/is/image/Target/GUEST_47330076-f287-4e1a-bc9f-2da8fe025414?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product20_img4 = Product_Image(product_id=20, image_url='https://target.scene7.com/is/image/Target/GUEST_ad17e188-6a0b-4d94-80c0-73d13749d785?qlt=85&fmt=webp&hei=700&fit=constrain')

    product21_img1 = Product_Image(product_id=21, image_url='https://target.scene7.com/is/image/Target/GUEST_7a830779-4611-4ef3-bd7b-612de825c05e?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product21_img2 = Product_Image(product_id=21, image_url='https://target.scene7.com/is/image/Target/GUEST_db30e692-60e1-44d5-aa32-dd802cd78b18?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product21_img3 = Product_Image(product_id=21, image_url='https://target.scene7.com/is/image/Target/GUEST_6e275ad1-c346-438a-a164-685c5d5ce89b?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product21_img4 = Product_Image(product_id=21, image_url='https://target.scene7.com/is/image/Target/GUEST_5532817d-7c98-4326-9146-37fa7d3aae20?qlt=85&fmt=webp&hei=700&fit=constrain')

    product22_img1 = Product_Image(product_id=22, image_url='https://target.scene7.com/is/image/Target/GUEST_6e9e73a9-32da-4e24-802b-51213742c2ac?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product22_img2 = Product_Image(product_id=22, image_url='https://target.scene7.com/is/image/Target/GUEST_1bb9ffb2-eed1-4f54-a512-1b24b7979329?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product22_img3 = Product_Image(product_id=22, image_url='https://target.scene7.com/is/image/Target/GUEST_c4c23014-3125-4d36-90f3-aa8ea3e233a2?wid=1000&hei=1000&qlt=80&fmt=webp')
    product22_img4 = Product_Image(product_id=22, image_url='https://target.scene7.com/is/image/Target/GUEST_d8f50e9b-797c-4c7a-85fd-4939b8d90e83?wid=1000&hei=1000&qlt=80&fmt=webp')

    product23_img1 = Product_Image(product_id=23, image_url='https://target.scene7.com/is/image/Target/GUEST_9f0b0120-4910-491c-9e64-146bef8eb040?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product23_img2 = Product_Image(product_id=23, image_url='https://target.scene7.com/is/image/Target/GUEST_15fa9e3c-f3ea-485c-a18f-b9987c6384bd?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product23_img3 = Product_Image(product_id=23, image_url='https://target.scene7.com/is/image/Target/GUEST_b60057f4-b703-49b6-a49b-8cac1617adca?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product23_img4 = Product_Image(product_id=23, image_url='https://target.scene7.com/is/image/Target/GUEST_94082b6b-eb68-4027-b554-34006dad42f0?wid=1000&hei=1000&qlt=80&fmt=webp')

    product24_img1 = Product_Image(product_id=24, image_url='https://target.scene7.com/is/image/Target/GUEST_94feb754-615e-4ab5-93f2-96f0cb7ae92c?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product24_img2 = Product_Image(product_id=24, image_url='https://target.scene7.com/is/image/Target/GUEST_b9ac5f16-e464-457c-8e32-b504717e3035?wid=1000&hei=1000&qlt=80&fmt=webp')
    product24_img3 = Product_Image(product_id=24, image_url='https://target.scene7.com/is/image/Target/GUEST_74968fd0-5947-428a-9cbc-0cdcc7a307c3?wid=1000&hei=1000&qlt=80&fmt=webp')
    product24_img4 = Product_Image(product_id=24, image_url='https://target.scene7.com/is/image/Target/GUEST_a64a6ca8-22bb-469c-806b-a5e39afa2b7b?wid=1000&hei=1000&qlt=80&fmt=webp')

   
    db.session.add(product13_img1)
    db.session.add(product13_img2)
    db.session.add(product13_img3)
    db.session.add(product13_img4)

    db.session.add(product14_img1)
    db.session.add(product14_img2)
    db.session.add(product14_img3)
    db.session.add(product14_img4)

    db.session.add(product15_img1)
    db.session.add(product15_img2)
    db.session.add(product15_img3)
    db.session.add(product15_img4)

    db.session.add(product16_img1)
    db.session.add(product16_img2)
    db.session.add(product16_img3)
    db.session.add(product16_img4)

    db.session.add(product17_img1)
    db.session.add(product17_img2)
    db.session.add(product17_img3)
    db.session.add(product17_img4)

    db.session.add(product18_img1)
    db.session.add(product18_img2)
    db.session.add(product18_img3)
    db.session.add(product18_img4)

    db.session.add(product19_img1)
    db.session.add(product19_img2)
    db.session.add(product19_img3)
    db.session.add(product19_img4)

    db.session.add(product20_img1)
    db.session.add(product20_img2)
    db.session.add(product20_img3)
    db.session.add(product20_img4)

    db.session.add(product21_img1)
    db.session.add(product21_img2)
    db.session.add(product21_img3)
    db.session.add(product21_img4)

    db.session.add(product22_img1)
    db.session.add(product22_img2)
    db.session.add(product22_img3)
    db.session.add(product22_img4)

    db.session.add(product23_img1)
    db.session.add(product23_img2)
    db.session.add(product23_img3)
    db.session.add(product23_img4)
  
    db.session.add(product24_img1)
    db.session.add(product24_img2)
    db.session.add(product24_img3)
    db.session.add(product24_img4)

    product25_img1 = Product_Image(product_id=25, image_url='https://target.scene7.com/is/image/Target/GUEST_1169d086-4142-4fc0-808c-a13d29d4eb2e?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product25_img2 = Product_Image(product_id=25, image_url='https://target.scene7.com/is/image/Target/GUEST_c9600d93-3bf7-4950-88cc-7e062d33fcc9?wid=1000&hei=1000&qlt=80&fmt=webp')
    product25_img3 = Product_Image(product_id=25, image_url='https://target.scene7.com/is/image/Target/GUEST_82f46db9-9dbf-40c7-80ae-65f98b99ffdc?wid=1000&hei=1000&qlt=80&fmt=webp')
    product25_img4 = Product_Image(product_id=25, image_url='https://target.scene7.com/is/image/Target/GUEST_c66d9e66-7920-430b-8474-78cdced07ae6?qlt=85&fmt=webp&hei=700&fit=constrain')

    product26_img1 = Product_Image(product_id=26, image_url='https://target.scene7.com/is/image/Target/GUEST_af5dec0a-c8a2-4993-91fc-69b17e5be176?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product26_img2 = Product_Image(product_id=26, image_url='https://target.scene7.com/is/image/Target/GUEST_238a02ff-3147-4fe2-8aaf-57b3f81418c9?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product26_img3 = Product_Image(product_id=26, image_url='https://target.scene7.com/is/image/Target/GUEST_b1846390-61ef-4eb8-a0c7-112f73f14abb?wid=1000&hei=1000&qlt=80&fmt=webp')
    product26_img4 = Product_Image(product_id=26, image_url='https://target.scene7.com/is/image/Target/GUEST_14c57d8c-119e-48ce-b97b-b0f1b99bf737?wid=1000&hei=1000&qlt=80&fmt=webp')

    product27_img1 = Product_Image(product_id=27, image_url='https://target.scene7.com/is/image/Target/GUEST_8e21bc85-fe95-47d6-b597-ec70dd580e34?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product27_img2 = Product_Image(product_id=27, image_url='https://target.scene7.com/is/image/Target/GUEST_71a4cd38-ca29-4915-9de2-08651a05f332?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product27_img3 = Product_Image(product_id=27, image_url='https://target.scene7.com/is/image/Target/GUEST_4700ab68-3037-4921-b763-4d8bb4b872b5?wid=1000&hei=1000&qlt=80&fmt=webp')
    product27_img4 = Product_Image(product_id=27, image_url='https://target.scene7.com/is/image/Target/GUEST_5fdb8ccf-3faa-4beb-979e-0e450aab65a4?wid=1000&hei=1000&qlt=80&fmt=webp')

    product28_img1 = Product_Image(product_id=28, image_url='https://target.scene7.com/is/image/Target/GUEST_60cd47ff-1c76-4b30-92dc-95854f3b5320?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product28_img2 = Product_Image(product_id=28, image_url='https://target.scene7.com/is/image/Target/GUEST_4254e750-546d-4403-9c72-69c91176a88a?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product28_img3 = Product_Image(product_id=28, image_url='https://target.scene7.com/is/image/Target/GUEST_e259b70e-a292-46d7-bd11-03d369bb1f80?wid=1000&hei=1000&qlt=80&fmt=webp')
    product28_img4 = Product_Image(product_id=28, image_url='https://target.scene7.com/is/image/Target/GUEST_8b1fa7fa-dec8-44a8-a401-4619ecd2f520?wid=1000&hei=1000&qlt=80&fmt=webp')

    product29_img1 = Product_Image(product_id=29, image_url='https://target.scene7.com/is/image/Target/GUEST_e4f2f735-06fd-42d7-8b41-60e90855122f?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product29_img2 = Product_Image(product_id=29, image_url='https://target.scene7.com/is/image/Target/GUEST_78984615-5028-4da0-af92-5d8301947d5a?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product29_img3 = Product_Image(product_id=29, image_url='https://target.scene7.com/is/image/Target/GUEST_e4f2f735-06fd-42d7-8b41-60e90855122f?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product29_img4 = Product_Image(product_id=29, image_url='https://target.scene7.com/is/image/Target/GUEST_78984615-5028-4da0-af92-5d8301947d5a?wid=325&hei=325&qlt=80&fmt=pjpeg')

    product30_img1 = Product_Image(product_id=30, image_url='https://target.scene7.com/is/image/Target/GUEST_08c03ec3-f566-44b5-814b-331f3029004f?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product30_img2 = Product_Image(product_id=30, image_url='https://target.scene7.com/is/image/Target/GUEST_e99ec229-06ce-4f35-9077-b96e5290ad82?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product30_img3 = Product_Image(product_id=30, image_url='https://target.scene7.com/is/image/Target/GUEST_ad812cde-c353-4d9f-8a3e-58d8bc1745c2?wid=1000&hei=1000&qlt=80&fmt=webp')
    product30_img4 = Product_Image(product_id=30, image_url='https://target.scene7.com/is/image/Target/GUEST_ed82e750-1cc6-4143-a315-4605a26d0f02?wid=1000&hei=1000&qlt=80&fmt=webp')

    product31_img1 = Product_Image(product_id=31, image_url='https://target.scene7.com/is/image/Target/GUEST_ff4240c9-5c7d-4f00-93f0-0e920c26e579?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product31_img2 = Product_Image(product_id=31, image_url='https://target.scene7.com/is/image/Target/GUEST_7b6d8653-4897-4987-91e3-8bbea7db665c?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product31_img3 = Product_Image(product_id=31, image_url='https://target.scene7.com/is/image/Target/GUEST_f31b1e4d-b740-4c8b-8a00-4822f3199613?wid=1000&hei=1000&qlt=80&fmt=webp')
    product31_img4 = Product_Image(product_id=31, image_url='https://target.scene7.com/is/image/Target/GUEST_4fa5a20e-68fe-4a44-b455-089bc2e341d4?wid=1000&hei=1000&qlt=80&fmt=webp')

    product32_img1 = Product_Image(product_id=32, image_url='https://target.scene7.com/is/image/Target/GUEST_70f281e0-e249-4d49-b136-e7d733fb7775?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product32_img2 = Product_Image(product_id=32, image_url='https://target.scene7.com/is/image/Target/GUEST_95e85140-5d42-4877-9576-c3294e2141d5?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product32_img3 = Product_Image(product_id=32, image_url='https://target.scene7.com/is/image/Target/GUEST_dc459349-44f7-44b0-84d0-39384f3832b2?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product32_img4 = Product_Image(product_id=32, image_url='https://target.scene7.com/is/image/Target/GUEST_8290b74e-89ee-40b4-92b9-fd1f84a8239f?wid=325&hei=325&qlt=80&fmt=pjpeg')

    product33_img1 = Product_Image(product_id=33, image_url='https://target.scene7.com/is/image/Target/GUEST_5c236d99-c907-41c5-a599-36422ea34c14?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product33_img2 = Product_Image(product_id=33, image_url='https://target.scene7.com/is/image/Target/GUEST_a313e252-1af1-4235-a144-16cbcc1e964a?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product33_img3 = Product_Image(product_id=33, image_url='https://target.scene7.com/is/image/Target/GUEST_6928a22d-50b0-461e-bced-e7085a5a3f05?wid=1000&hei=1000&qlt=80&fmt=webp')
    product33_img4 = Product_Image(product_id=33, image_url='https://target.scene7.com/is/image/Target/GUEST_b76e5fca-8b5e-42f8-832e-998526aca0c9?wid=1000&hei=1000&qlt=80&fmt=webp')

    product34_img1 = Product_Image(product_id=34, image_url='https://target.scene7.com/is/image/Target/GUEST_4bdc45d2-b1b1-419a-9029-356f8190f5ad?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product34_img2 = Product_Image(product_id=34, image_url='https://target.scene7.com/is/image/Target/GUEST_1f30392e-d034-461d-9107-536e05bc7dc6?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product34_img3 = Product_Image(product_id=34, image_url='https://target.scene7.com/is/image/Target/GUEST_da43db77-2b15-48f1-a177-5819dd25688d?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product34_img4 = Product_Image(product_id=34, image_url='https://target.scene7.com/is/image/Target/GUEST_bf613406-0f4c-459d-91c0-1d770f91fe8a?wid=1000&hei=1000&qlt=80&fmt=webp')

    product35_img1 = Product_Image(product_id=35, image_url='https://target.scene7.com/is/image/Target/GUEST_a9577e57-9613-4e24-b0a3-a610392bcf85?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product35_img2 = Product_Image(product_id=35, image_url='https://target.scene7.com/is/image/Target/GUEST_74e35c26-587f-4c07-9495-a800dd0a2ef6?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product35_img3 = Product_Image(product_id=35, image_url='https://target.scene7.com/is/image/Target/GUEST_a42e34d8-47b1-4cef-a6b1-a2020a336045?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product35_img4 = Product_Image(product_id=35, image_url='https://target.scene7.com/is/image/Target/GUEST_f5f49c61-f595-4d34-bbcf-5b96f91d3216?wid=1000&hei=1000&qlt=80&fmt=webp')

    product36_img1 = Product_Image(product_id=36, image_url='https://target.scene7.com/is/image/Target/GUEST_ee704157-8ca8-44b8-807d-61ed7363f9dd?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product36_img2 = Product_Image(product_id=36, image_url='https://target.scene7.com/is/image/Target/GUEST_2dc179ec-ca13-4ee3-94ee-1daf52117fb0?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product36_img3 = Product_Image(product_id=36, image_url='https://target.scene7.com/is/image/Target/GUEST_69436ece-6b75-40e4-a70e-5a25d0ee6997?wid=325&hei=325&qlt=80&fmt=pjpeg')
    product36_img4 = Product_Image(product_id=36, image_url='https://target.scene7.com/is/image/Target/GUEST_42fd1f0d-d84c-4a86-b097-daf2ac4f19f4?qlt=85&fmt=webp&hei=700&fit=constrain')

    db.session.add(product25_img1)
    db.session.add(product25_img2)
    db.session.add(product25_img3)
    db.session.add(product25_img4)

    db.session.add(product26_img1)
    db.session.add(product26_img2)
    db.session.add(product26_img3)
    db.session.add(product26_img4)

    db.session.add(product27_img1)
    db.session.add(product27_img2)
    db.session.add(product27_img3)
    db.session.add(product27_img4)

    db.session.add(product28_img1)
    db.session.add(product28_img2)
    db.session.add(product28_img3)
    db.session.add(product28_img4)

    db.session.add(product29_img1)
    db.session.add(product29_img2)
    db.session.add(product29_img3)
    db.session.add(product29_img4)

    db.session.add(product30_img1)
    db.session.add(product30_img2)
    db.session.add(product30_img3)
    db.session.add(product30_img4)

    db.session.add(product31_img1)
    db.session.add(product31_img2)
    db.session.add(product31_img3)
    db.session.add(product31_img4)

    db.session.add(product32_img1)
    db.session.add(product32_img2)
    db.session.add(product32_img3)
    db.session.add(product32_img4)

    db.session.add(product33_img1)
    db.session.add(product33_img2)
    db.session.add(product33_img3)
    db.session.add(product33_img4)

    db.session.add(product34_img1)
    db.session.add(product34_img2)
    db.session.add(product34_img3)
    db.session.add(product34_img4)

    db.session.add(product35_img1)
    db.session.add(product35_img2)
    db.session.add(product35_img3)
    db.session.add(product35_img4)
  
    db.session.add(product36_img1)
    db.session.add(product36_img2)
    db.session.add(product36_img3)
    db.session.add(product36_img4)

    db.session.commit()


def undo_product_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.product_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM product_images")
        db.session.commit()