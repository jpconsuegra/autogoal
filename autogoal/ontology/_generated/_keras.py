# AUTOGENERATED ON 2019-12-27 10:53:31.364352
## DO NOT MODIFY THIS FILE MANUALLY


from keras.layers import *
from ..base import register_concrete_class
from ..base import Discrete
from ..base import Continuous


@register_concrete_class
class ActivityRegularizationLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = ActivityRegularization


@register_concrete_class
class AddLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = Add


@register_concrete_class
class AlphaDropoutLayer(BaseObject, Layer):
	def __init__(
		self,
		rate: Continuous(0.0, 1.0),
	):
		self.keras_class = AlphaDropout
		self.rate = rate


@register_concrete_class
class AverageLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = Average


@register_concrete_class
class AveragePooling1DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = AveragePooling1D


@register_concrete_class
class AveragePooling2DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = AveragePooling2D


@register_concrete_class
class AveragePooling3DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = AveragePooling3D


@register_concrete_class
class AveragePooling1DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = AveragePooling1D


@register_concrete_class
class AveragePooling2DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = AveragePooling2D


@register_concrete_class
class AveragePooling3DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = AveragePooling3D


@register_concrete_class
class BatchNormalizationLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = BatchNormalization


@register_concrete_class
class ConcatenateLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = Concatenate


@register_concrete_class
class Cropping1DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = Cropping1D


@register_concrete_class
class Cropping2DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = Cropping2D


@register_concrete_class
class Cropping3DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = Cropping3D


@register_concrete_class
class DenseLayer(BaseObject, Layer):
	def __init__(
		self,
		units: Discrete(0, 100),
	):
		self.keras_class = Dense
		self.units = units


@register_concrete_class
class DropoutLayer(BaseObject, Layer):
	def __init__(
		self,
		rate: Continuous(0.0, 1.0),
	):
		self.keras_class = Dropout
		self.rate = rate


@register_concrete_class
class ELULayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = ELU


@register_concrete_class
class EmbeddingLayer(BaseObject, Layer):
	def __init__(
		self,
		input_dim: Discrete(0, 100),
		output_dim: Discrete(0, 100),
	):
		self.keras_class = Embedding
		self.input_dim = input_dim
		self.output_dim = output_dim


@register_concrete_class
class FlattenLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = Flatten


@register_concrete_class
class GaussianDropoutLayer(BaseObject, Layer):
	def __init__(
		self,
		rate: Continuous(0.0, 1.0),
	):
		self.keras_class = GaussianDropout
		self.rate = rate


@register_concrete_class
class GaussianNoiseLayer(BaseObject, Layer):
	def __init__(
		self,
		stddev: Continuous(0.0, 1.0),
	):
		self.keras_class = GaussianNoise
		self.stddev = stddev


@register_concrete_class
class GlobalAveragePooling1DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = GlobalAveragePooling1D


@register_concrete_class
class GlobalAveragePooling2DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = GlobalAveragePooling2D


@register_concrete_class
class GlobalAveragePooling3DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = GlobalAveragePooling3D


@register_concrete_class
class GlobalAveragePooling1DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = GlobalAveragePooling1D


@register_concrete_class
class GlobalAveragePooling2DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = GlobalAveragePooling2D


@register_concrete_class
class GlobalAveragePooling3DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = GlobalAveragePooling3D


@register_concrete_class
class GlobalMaxPooling1DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = GlobalMaxPooling1D


@register_concrete_class
class GlobalMaxPooling2DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = GlobalMaxPooling2D


@register_concrete_class
class GlobalMaxPooling3DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = GlobalMaxPooling3D


@register_concrete_class
class GlobalMaxPooling1DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = GlobalMaxPooling1D


@register_concrete_class
class GlobalMaxPooling2DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = GlobalMaxPooling2D


@register_concrete_class
class GlobalMaxPooling3DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = GlobalMaxPooling3D


@register_concrete_class
class InputLayerLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = InputLayer


@register_concrete_class
class LeakyReLULayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = LeakyReLU


@register_concrete_class
class MaskingLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = Masking


@register_concrete_class
class MaxPooling1DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = MaxPooling1D


@register_concrete_class
class MaxPooling2DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = MaxPooling2D


@register_concrete_class
class MaxPooling3DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = MaxPooling3D


@register_concrete_class
class MaxPooling1DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = MaxPooling1D


@register_concrete_class
class MaxPooling2DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = MaxPooling2D


@register_concrete_class
class MaxPooling3DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = MaxPooling3D


@register_concrete_class
class MaximumLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = Maximum


@register_concrete_class
class MinimumLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = Minimum


@register_concrete_class
class MultiplyLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = Multiply


@register_concrete_class
class PReLULayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = PReLU


@register_concrete_class
class ReLULayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = ReLU


@register_concrete_class
class RecurrentLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = Recurrent


@register_concrete_class
class RepeatVectorLayer(BaseObject, Layer):
	def __init__(
		self,
		n: Discrete(0, 100),
	):
		self.keras_class = RepeatVector
		self.n = n


@register_concrete_class
class SoftmaxLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = Softmax


@register_concrete_class
class SubtractLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = Subtract


@register_concrete_class
class ThresholdedReLULayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = ThresholdedReLU


@register_concrete_class
class UpSampling1DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = UpSampling1D


@register_concrete_class
class UpSampling2DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = UpSampling2D


@register_concrete_class
class UpSampling3DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = UpSampling3D


@register_concrete_class
class ZeroPadding1DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = ZeroPadding1D


@register_concrete_class
class ZeroPadding2DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = ZeroPadding2D


@register_concrete_class
class ZeroPadding3DLayer(BaseObject, Layer):
	def __init__(
		self,
	):
		self.keras_class = ZeroPadding3D


