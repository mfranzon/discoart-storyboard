from jina import Client

c = Client(host='grpc://0.0.0.0:51001')

def text_to_image(chapter, story_title, ind):

    da = c.post(on='/create',
                parameters={
                    'name_docarray': story_title + f"-Chapter-{ind}",
                    'text_prompts': [
                        chapter[0]["summary_text"],
                    ],
                    'n_batches' : 1,
                    'diffusion_model' : '256x256_diffusion_uncond',
                    'steps' : 200,
                    'width_height' : [256,256]
                },
    )
