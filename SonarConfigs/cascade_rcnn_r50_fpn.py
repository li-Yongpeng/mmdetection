_base_ = [
    '../configs/_base_/models/cascade_rcnn_r50_fpn.py',
    '../configs/_base_/datasets/voc0712.py',
    '../configs/_base_/default_runtime.py'
]


# optimizer
optimizer = dict(type='SGD', lr=0.002, momentum=0.9, weight_decay=0.001)
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.001,
    step=[8, 11])
total_epochs = 12

