def text_to_image(backend, server,
                 chapter, story_title, ind, style):

    if backend=="DiscoArt":
        from jina import Client

        c = Client(host=server)

        da = c.post(on='/create',
                    parameters={
                        'name_docarray': story_title + f"-Chapter-{ind}",
                        'text_prompts': [
                            f'{chapter[0]["summary_text"]}, {style}',
                        ],
                        'n_batches' : 2,
                        'diffusion_model' : '256x256_diffusion_uncond',
                        'steps' : 200,
                        'width_height' : [256,256]
                    },
        )
        
    elif backend=="DALLE-Flow":
        from io import BytesIO
        from PIL import Image
        from docarray import Document

        dalle_flow_url = server

        doc = Document(text=f'{chapter[0]["summary_text"]}, {style}').post(dalle_flow_url,
                                                parameters={'num_images': 1})
        doc_imgs = doc.matches
    
        dalle_img = doc_imgs[0].load_uri_to_blob()
        b_dalle_img = Image.open(BytesIO(dalle_img.blob))
        b_dalle_img.save(f"{story_title}-Chapter-{ind}.png", "PNG")
    
    else:
        pass